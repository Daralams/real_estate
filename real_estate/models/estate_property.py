from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread']
    _description = 'Estate Property'
    _order = "id desc"

    name = fields.Char(string="Name", required=True, help='Name of property')
    tags = fields.Many2many('estate.property.tag', string="Tags", help="Tags of property", ondelete="cascade")
    property_type_id = fields.Many2one('estate.property.type', string="Type", help='Type of property', required=True, ondelete="cascade")
    country_id = fields.Many2one('res.country', string="Country", required=True)
    postcode = fields.Char(string="Postcode", required=True, help='Property Post Code')
    available_date = fields.Date(string="Available From", required=True, help='Available date property', default=lambda self:date.today() +timedelta(days=90), copy=False)
    expected_price = fields.Float(string="Expected Price", required=True, help='Property Expected price')
    best_offer = fields.Float(string="Best Offer", help='Property price Best offer', compute="_compute_best_offer")
    sell_price = fields.Float(string="Selling Price", help='Property selling price', copy=False)
    state = fields.Selection([
        ("new", "New"),
        ("offer received", "Offer Received"),
        ("offer accepted", "Offer Accepted"),
        ("sold", "Sold"),
        ("cancelled", "Cancelled"),
    ], string="Status", required=True, default="new", tracking=True)
    active = fields.Boolean(string="Active", help="This record is active or inactive")
    description = fields.Text(string="Description")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=True)
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden area (sqm)")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation")
    total_area = fields.Integer(string="Total area", compute="_total_area")
    salesman = fields.Many2one('res.users', string="Salesman", default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', string="Buyer")
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id')


    _sql_constraints = [
        ('expected_price', 'CHECK(expected_price > 0)', 'Expected price should be strictly positive!'),
    ]

     # action server 
    def set_to_cancell(self):
        for record in self:
            if record.state not in "cancelled":
                record.state = "cancelled"
            else:
                raise ValidationError("State must be not in cancelled.")

    def set_as_new(self):
        for record in self:
            if record.state == "cancelled" and record.state not in "new":
                record.state = "new"
            else:
                raise ValidationError("State must be in cancelled.")

    def get_estate_property_excel_report(self):
        # redirect ke controller route: /download/estate-property-report-excel/
        return {
            'type': 'ir.actions.act_url',
            'url': '/download/estate-property-report-excel/%s' % (self.id),
            'target': 'new'
        }

    def wizard_test(self):
        """This function is called when the user clicks the
        'Export Excel' button on a estate property's form view. It opens a
        new wizard export excel."""
        return {
            'type': 'ir.actions.act_window',
            'name': _('Wizard Test'),
            'res_model': 'estate.custom.wizard',
            'target': 'new',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {'default_user_id': self.id} # ini pentingkah?
        }

    def action_sold(self):
        self.state = "sold"

    def action_cancel(self):
        self.state = "cancelled"

    @api.depends('best_offer', 'description', 'offer_ids.partner_id')
    def _compute_best_offer(self):
        for record in self:
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0 
        
    @api.constrains('living_area')
    def _min_length_living_area(self):
        for record in self:
            if record.living_area <= 5:
                raise ValidationError("The area of ​​the living room must be more than 5 meters")
            
    @api.constrains('sell_price')
    def _min_selling_price(self):
        min_sell_price = self.expected_price * 0.9
        if self.sell_price < min_sell_price: 
            raise ValidationError("The selling price must be at least 90% of the expected price! You must reduce the expected price if you want to accept this offer.")

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""


    @api.depends('total_area')
    def _total_area(self):
        self.total_area = self.living_area + self.garden_area

    # override
    def unlink(self):
        for record in self:
            if record.state == 'sold' or record.state == 'cancelled':
                raise ValidationError("Sold or Cancelled property cannot be delete!")
            return super(EstateProperty, self).unlink()
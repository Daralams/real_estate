from odoo import models, fields, api
from datetime import date, timedelta
from odoo.exceptions import ValidationError

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    _order = "price desc"

    property_id = fields.Many2one('estate.property', ondelete="cascade")
    property_type_id = fields.Many2one('estate.property.type', string="Type", ondelete="cascade", help="Type of the property")
    price = fields.Float(string="Price")
    partner_id = fields.Many2one('res.partner', string="Partner")
    validity = fields.Integer(string="Validity (days)", default=7, required=True)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string="Status",  copy=False)
    offer_state = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done'),
    ], default="pending", help="Control visibility of the button")
    
    _sql_constraints = [
        ('check_validity', 'CHECK(validity >= 0)', 'Validity must be positive!')
    ]

    @api.depends("date_deadline")
    def _compute_date_deadline(self):
        for record in self:
            if record.validity:
                record.date_deadline = date.today() +timedelta(days=record.validity)
            else:
                record.date_deadline = date.today()

    def _inverse_date_deadline(self):
        for record in self:
            record.date_deadline = record.date_deadline

    # override
    @api.model
    def create(self, vals):
        record = super(EstatePropertyOffer, self).create(vals)
        if record.property_id:
            record.property_id.state = 'offer received'
        return record

    def accept_offer(self):
        for record in self:
            record.status = "accepted"
            record.property_id.sell_price = record.price
            record.property_id.state = "offer accepted"
            record.property_id.buyer = record.partner_id
            record.offer_state = "done"
        

    def refused_offer(self):
        for record in self:
            record.status = "refused"
            record.offer_state = "done"

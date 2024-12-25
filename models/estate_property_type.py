from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'id desc'

    name = fields.Char(string="Type", help="Type of property")
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='property_type_id', string="Properties")
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_type_id', string="Offers")
    offer_count = fields.Integer(string="Offer Count", compute="_compute_offer_count")
    sequence = fields.Integer('Sequence', default=1)

    _sql_constraints = [
        ('name', 'UNIQUE(name)', 'Name of property type must be unique')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for offers in self:
            if offers.offer_ids:
                all_offer = [offer.id for offer in offers.offer_ids]
                offers.offer_count = len(all_offer)
            else:
                offers.offer_count = 0

    
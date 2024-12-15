from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'id desc'

    name = fields.Char(string="Type", help="Type of property")
    property_ids = fields.One2many('estate.property', 'property_type_id', string="Properties", readonly=True)
    sequence = fields.Integer('Sequence', default=1)

    _sql_constraints = [
        ('name', 'UNIQUE(name)', 'Name of property type must be unique')
    ]
    
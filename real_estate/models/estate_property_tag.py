from odoo import models, fields, api

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Type'

    name = fields.Char(string="Name", help="The property tag")
    color = fields.Integer(string="Color")
    sequence = fields.Integer('Sequence', default=1)

    _sql_constraints = [
        ('name', 'UNIQUE(name)', 'Name of property tag must be unique')
    ]
    
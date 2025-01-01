from odoo import models, fields, api

class EstateBaseUserInherit(models.Model):
    _inherit = 'res.users'
    _description = 'Estate Base User Inherit'

    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='salesman', string="Properties")
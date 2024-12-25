from odoo import models, fields, api

class EstateBaseUserInherit(models.Model):
    _inherit = 'res.users'
    _description = 'Estate Base User Inherit'

    property_ids = fields.One2many('estate.property', 'salesman', string="Properties")
from odoo import models, fields, api

class MyTransientModel(models.TransientModel):
    _name = 'my.transient.model'
    _description = 'My Transient Model'

    name = fields.Char(string="Name", store=False)
    type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
    ], string="Type")
    date = fields.Date(string="Date", readonly=True, default=fields.date.today())

    # @api.autovacumm
    # def _transient_vacumm(self):
    #     if self._transient_max_hours:
    #         # Age-based expiration
    #         self._transient_clean_rows_older_than(self._transient_max_hours * 60 * 60)
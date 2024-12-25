from odoo import models, fields, Command, api

class EstatePropertyInherit(models.Model):
    _inherit = 'estate.property'
    _description = 'Estate property inherit'

    def action_sold(self):
        administrative_fees = 100.00
        self.env["account.move"].create(
            {
                "partner_id": self.buyer.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [
                    Command.create({
                        "name": self.name,
                        "quantity": 1,
                        "price_unit": self.sell_price + administrative_fees
                    })
                ]
            }
        )
        return super(EstatePropertyInherit, self).action_sold()
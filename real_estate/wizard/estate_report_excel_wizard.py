from odoo import models, fields, api, _

class EstateCustomWizard(models.TransientModel):
    _name = 'estate.custom.wizard'
    _description = 'Estate Custom Wizard'

    needs = fields.Text(string="Needs", required=True)

    def testing(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Hore hore")

    # def estate_report_excel_act(self):
    #     """This function is called when the user clicks the
    #     'Export Excel' button on a estate property's form view. It opens a
    #     new wizard export excel."""
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': _('Export Excel'),
    #         'res_model': 'estate.property',
    #         'target': 'new',
    #         'view_mode': 'form',
    #         'view_type': 'form',
    #         'context': {'default_user_id': self.id} # ini pentingkah?
    #     }

    # def get_estate_property_excel_report(self):
    #     # redirect ke controller route: /download/estate-property-report-excel/
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': '/download/estate-property-report-excel/%s' % (self.id),
    #         'target': 'new'
    #     }
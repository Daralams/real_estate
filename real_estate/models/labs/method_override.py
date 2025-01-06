from odoo import models, fields, api
from odoo.exceptions import ValidationError
from num2words import num2words  # fungsi terbilang untuk merubah value int / float menjadi bahasa. contoh: 100 = seratus

class MethodOverride(models.Model):
    _inherit = 'estate.property'


    # override
    @api.model
    def create(self, vals):
        print(">>>>>>>>>>>>>>> fungsi terbilang: ", num2words(vals.get('expected_price'), lang="id"))
        print(">>>>>>>>>>>>>>> result create: ", vals)
        print(">>>>>>>>>>>>>>> desc: ", vals.get('description'))
        if not vals.get('description', False):
            vals['description'] = 'Di isi otomatis pake method override create'

        minimum_price = vals.get('expected_price')
        if minimum_price < 5000:
            raise ValidationError("Expected price must be longer than 5000!")

        res = super(MethodOverride, self).create(vals)
        return res

    # def write(self, vals):
    #     if vals.get('name', 'example 2'):
    #         vals['name'] = 'example 2 edited!'

    #     # jika expected_price dirubah
    #     if vals.get('expected_price'):
    #         # cek apakah ada offer dan offer tsb sdh di accept, jika ada dan sdh di accept jangan izinkan write
    #         offer_accepted = self.env['estate.property.offer'].search([('property_id', '=', self.id), ('status', '=', 'accepted')])
    #         if offer_accepted:
    #             raise ValidationError('You cannot change the price of this property, because this property has already been offer by the buyer and has been approved by the seller')

    #     if vals.get('description', 'Di isi otomatis pake method override create'):
    #         vals['description'] = 'Di isi otomatis pake method override write'

    #     res = super(MethodOverride, self).write(vals)
    #     return res
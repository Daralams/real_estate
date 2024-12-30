from odoo import http, models, fields, _
from odoo.http import request
import json

class EstatePropertyWebController(http.Controller):
    @http.route([
        '''/estate''', 
        '''/estate/<model("estate.property", "[('id', '=', 'property_id')]"):property_id>''', 
        '''/estate/<model("estate.property", "[('id', '=', 'property_id')]"):property_id>/<int:property_offers>'''
    ], type="http", auth="user", csrf=False)
    def get_property(self, property_id=None, property_offers=None, **args):
        value = []
      
        if not property_id and not property_offers:
            properties = request.env['estate.property'].search([])
            for property in properties:
                value.append({
                    'property_id': property.id,
                    'name': property.name,
                    'price': property.expected_price
                })
        else:
            if property_id:
                value = {
                    'property_id': property_id.id,
                    'name': property_id.name,
                    'price': property_id.expected_price 
                }

                if property_offers:
                    offers = []
                    for offer in property_id.offer_ids:
                        offers.append({
                            'price': offer.price,
                            'partner_id': offer.partner_id.name,
                            'validity (days)': offer.validity, 
                            'deadline': offer.date_deadline.isoformat(),  # convert ke format string ISO 8601
                            'status': offer.status
                        })
                    value.update({ 'offers': offers })

        return json.dumps(value)
from odoo import http, models, fields
from odoo.http import request

class EstatePropertyFormCreate(http.Controller):
    @http.route('/estate-property/advertiments/create', type="http", auth="user", csrf=True, website=True)
    def render_create_form(self, **args):
        return request.render('real_estate.estate_property_web_create')

class EstatePropertyProcessCreate(http.Controller):
    @http.route('/process-create', type="http", auth="user", csrf=True, website=True)
    def process_create(self, **args):
        data = {
            'messege': 'Create type Property successfully!'
        }

        try:
            create_type = request.env['estate.property.type'].sudo().create({
                'name': args.get('name', '')
            })
        except Exception:
            data['messege'] = 'Sorry something wrong, please try again!'

        return request.render('real_estate.estate_property_web_response', data)
from odoo import http, models, fields, _
from odoo.http import request

class EstatePropertyWebTemplateController(http.Controller):
    @http.route('/estate-property/advertisment', type="http", auth="user", website=True)
    def get_properties_advertisment(self, **args):
        properties = request.env['estate.property'].search([])
        data = {
            'properties': properties
        }
        return request.render('real_estate.estate_property_web_template', data)
    
class EstatePropertyContactController(http.Controller):
    @http.route('/estate-property/contact', type="http", auth="user", website=True)
    def handle_contact_route(self, **args):
        return request.render('real_estate.estate_property_contact_form')


class EstatePropertySendMessegeController(http.Controller):
    @http.route('/estate-property/contact/response', type="http", auth="user", website=True)
    def get_data_user_req(self, **args):
        data = {
            'name': args.get('name', ''),
            'email': args.get('email', ''),
            'messege': args.get('messege', ''),
        }
        return request.render('real_estate.estate_property_contact_response', data)



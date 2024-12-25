# -*- coding: utf-8 -*-
# from odoo import http


# class RealEstateAccount(http.Controller):
#     @http.route('/real_estate_account/real_estate_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_account/real_estate_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_account.listing', {
#             'root': '/real_estate_account/real_estate_account',
#             'objects': http.request.env['real_estate_account.real_estate_account'].search([]),
#         })

#     @http.route('/real_estate_account/real_estate_account/objects/<model("real_estate_account.real_estate_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_account.object', {
#             'object': obj
#         })


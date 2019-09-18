# -*- coding: utf-8 -*-
from openerp import http
import sys, os
class TreeAddButton(http.Controller):
    @http.route('/w/product_import_qw/', type='http', csrf=False, auth='user')
    def w_product_import_csv(self, **kwargs):
           return http.send_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'import.xlsx'),
                          filename='import.xlsx', as_attachment=True)
#     @http.route('/tree_add_button/tree_add_button/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tree_add_button/tree_add_button/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tree_add_button.listing', {
#             'root': '/tree_add_button/tree_add_button',
#             'objects': http.request.env['tree_add_button.tree_add_button'].search([]),
#         })

#     @http.route('/tree_add_button/tree_add_button/objects/<model("tree_add_button.tree_add_button"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tree_add_button.object', {
#             'object': obj
#         })

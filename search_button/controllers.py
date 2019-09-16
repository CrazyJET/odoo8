# -*- coding: utf-8 -*-
from openerp import http

# class SearchButton(http.Controller):
#     @http.route('/search_button/search_button/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/search_button/search_button/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('search_button.listing', {
#             'root': '/search_button/search_button',
#             'objects': http.request.env['search_button.search_button'].search([]),
#         })

#     @http.route('/search_button/search_button/objects/<model("search_button.search_button"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('search_button.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from odoo import http

# class Cineplex(http.Controller):
#     @http.route('/cineplex/cineplex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cineplex/cineplex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cineplex.listing', {
#             'root': '/cineplex/cineplex',
#             'objects': http.request.env['cineplex.cineplex'].search([]),
#         })

#     @http.route('/cineplex/cineplex/objects/<model("cineplex.cineplex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cineplex.object', {
#             'object': obj
#         })
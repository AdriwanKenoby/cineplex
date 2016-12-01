# -*- coding: utf-8 -*-

from odoo import models, fields, api

class City(models.Model):
    _name = 'cineplex.city'

    name = fields.Char(required=True)
    cp = fields.Integer(required=True)


class Site(models.Model):
    _name = 'cineplex.site'

    name = fields.Char(required=True)
    city_id = fields.Many2one('cineplex.city', ondelete='set null', string='City', index=True)

class Salle(models.Model):
    _name = 'cineplex.salle'

    site_id = fields.Many2one('cineplex.site', ondelete='set null', string='Site', index=True)

class Film(models.Model):
    _name = 'cineplex.film'

    name = fields.Char(required=True)
    seance_id = fields.Many2one('cineplex.seance', ondelete='cascade', string='Seance', index=True)

class Seance(models.Model):
    _name = 'cineplex.seance'

    start_date = fields.Date()
    duration = fields.Float()
    seats = fileds.Integer()

    salle_id = fields.Many2one('cineplex.salle', ondelete='set null', string='Salle', index=True)
    film_id = fields.Many2one('cineplex.film', ondelete='set null', string='Film', index=True, required=True)

# class cineplex(models.Model):
#     _name = 'cineplex.cineplex'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

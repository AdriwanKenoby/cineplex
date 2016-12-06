# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class City(models.Model):
    _name = 'cineplex.city'

    name = fields.Char(required=True)
    cp = fields.Integer(string="Code Postal",required=True)


class Site(models.Model):
    _name = 'cineplex.site'

    name = fields.Char(required=True)
    city_id = fields.Many2one('cineplex.city', ondelete='set null', string='City', index=True)

class Salle(models.Model):
    _name = 'cineplex.salle'
    
    name = fields.Char(required=True)
    nb_place = fields.Integer(string = "Nombre de place")
    site_id = fields.Many2one('cineplex.site', ondelete='set null', string='Site', index=True)
    nb_place_rest=fields.Integer(string = "Nombre de place restees", compute="_nb_place_rest")
    seance_id = fields.One2many('cineplex.seance', 'salle_id',string="Seance")
    

    @api.depends('nb_place', 'seance_id.seats')
    def _nb_place_rest(self):
        for r in self:
            r.nb_place_rest = r.nb_place - r.seance_id.seats
 
    @api.constrains('nb_place')
    def _verify_nb_place(self):
	for r in self:
            if( r.nb_place <= 0):
	        raise exceptions.ValidationError("Le Nombre de place doit etre superieur a 0")


class Film(models.Model):
    _name = 'cineplex.film'

    name = fields.Char(string="Titre",required=True)    

class Seance(models.Model):
    _name = 'cineplex.seance'

   
    start_date = fields.Date(string="Date de debut",default=fields.Date.today)
    duration = fields.Float(string="Duration in hours", help="Duree en heure (1,5 = 1h et 30 minutes)",required=True)
    seats = fields.Integer(string = "Nombre de place reservees", required=True)

    salle_id = fields.Many2one('cineplex.salle', ondelete='set null', string='Salle', index=True, required=True)
    film_id = fields.Many2one('cineplex.film', ondelete='set null', string='Film', index=True, required=True)

    @api.constrains('seats','duration')
    def _verify_seats(self):
	for r in self:
            if( r.salle_id.nb_place - r.seats < 0 or r.seats <= 0):
	        raise exceptions.ValidationError("=>Verifier la disponibilite des places!\n=>Le Nombre de place a reserve doit etre superieur a 0")    
            if( r.duration == 0):
	        raise exceptions.ValidationError("La Duree doit etre sup a 0") 
    
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

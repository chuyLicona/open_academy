from odoo import models, fields, api


class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    name = fields.Char(string="Name", required=True)
    startD = fields.Text()
    duration= fields.Text()
    noSeats= fields.Text()
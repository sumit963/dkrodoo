from odoo import fields, models

class IshaMeditator(models.Model):
    _name = 'isha.meditator'

    name = fields.Char(string="Name", required=True)
    dob = fields.Date(string="DoB")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender")
    programs = fields.Many2many(comodel_name='isha.program', string="Programs")
    level = fields.Selection([('0', ''), ('basic', 'Basic'),('intermediate', 'Intermediate'), ('advanced', 'Advanced')], string='Level')
    interested_in_it = fields.Boolean("Interested in IT?")
    address = fields.Text(string="Address")
    active = fields.Boolean("Active")
    localcenter = fields.Char(string="Local Center")
    iecdate = fields.Date(string="IE Completion Date")
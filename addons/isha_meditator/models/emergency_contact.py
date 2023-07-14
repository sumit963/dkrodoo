from odoo import fields, models

class EmergencyContact(models.Model):
    _name = 'emergency.contact'

    relationtype = fields.Selection([('spouse', 'Spouse'),('sister', 'Sister'),('brother', 'Brother'),('father', 'Father'),('mother', 'Mother')])
    name = fields.Char(string="Name", required=True)
    contactnumber = fields.Char(string="Name")
    address = fields.Text(string="Address")
    
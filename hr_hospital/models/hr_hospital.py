from odoo import models, fields


class HrHospital(models.Model):
    _name = 'hr.hospital'
    _description = 'Hospital'
    name = fields.Char(string='Hospital name')

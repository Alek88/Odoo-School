from odoo import models, fields


class HrHospital(models.Model):
    _name = 'hr.hospital'
    name = fields.Char(string='Hospital')

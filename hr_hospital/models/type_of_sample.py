from odoo import models, fields


class HrHospitalTypeOfSample(models.Model):
    _name = 'hr.hospital.type.of.sample'
    _description = "Type of sample"
    active = fields.Boolean(default=True)
    name = fields.Char()
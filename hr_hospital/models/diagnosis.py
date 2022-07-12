from odoo import models, fields


class HrHospitalDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    name = fields.Char(string='Diagnose name')

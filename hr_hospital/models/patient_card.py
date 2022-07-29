from odoo import models, fields


class HrHospitalPatientCard(models.Model):
    _name = 'hr.hospital.patient.card'
    _description = 'Patient card'
    active = fields.Boolean(default=True)
    name = fields.Char(string='Patient card name')
    disease_history = fields.Char()
    partient = fields.Many2one(string='Patient', 
                               comodel_name='hr.hospital.patient')

from odoo import models, fields


class HrHospitalDiseaseHistory(models.Model):
    _name = 'hr.hospital.disease.history'
    _description = 'Disease History'
    name = fields.Char()
    active = fields.Boolean(default=True)
    date = fields.Date()
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    disease_ids = fields.Many2many(comodel_name='hr.hospital.disease')
    
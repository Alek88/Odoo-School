from email.policy import default
from odoo import models, fields, api


class HrHospitalAnalisis(models.Model):
    _name = 'hr.hospital.analisis'
    _description = 'Analisis'
    name = fields.Char()
    active = fields.Boolean(default=True)
    date = fields.Date(default=fields.Date.today)
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    disease_id = fields.Many2one(comodel_name='hr.hospital.disease')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    type_of_sample_id = fields.Many2one(comodel_name='hr.hospital.type.of.sample')
    
    patient_name = fields.Char(compute='get_patient_phone_name', store=True)
    patient_phone = fields.Char(compute='get_patient_phone_name', store=True)
    
    @api.depends('patient_id')
    def get_patient_phone_name(self):
        for record in self:
            if record.patient_id.id:
                record.patient_name = record.patient_id.name
                record.patient_phone = record.patient_id.phone
            else:
                record.patient_name = ""
                record.patient_phone = ""
    
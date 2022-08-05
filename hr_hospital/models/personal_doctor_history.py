from odoo import models, fields, api


class HrHospitalPersonalDoctorHistory(models.Model):
    _name = 'hr.hospital.pers.doc.history'
    _description = "Personal doctor history"
    active = fields.Boolean(default=True)
    name = fields.Char()
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient', 
                                 index=True)
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                index=True)
    date = fields.Datetime()

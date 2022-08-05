from odoo import models, fields


class HrHospitalDoctorVisit(models.Model):
    _name = 'hr.hospital.doctor.visit'
    _description = "Doctor's visit"
    active = fields.Boolean(default=True)
    name = fields.Char()
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)
    visit_date = fields.Datetime(default=fields.Date.today)
    stop_visit_date = fields.Datetime(default=fields.Date.today)
    diagnosis_id = fields.Many2one(comodel_name='hr.hospital.diagnosis')
    research_id = fields.Many2one(comodel_name='hr.hospital.research')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient',
                                 required = True)
    recomendation = fields.Text(string='Recomendation')

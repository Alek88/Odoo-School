from odoo import models, fields


class HrHospitalResearch(models.Model):
    _name = 'hr.hospital.research'
    _description = "Pesearch"
    active = fields.Boolean(default=True)
    name = fields.Char()
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    type_research_ids = fields.Many2many(comodel_name='hr.hospital.type.of.research')
    type_sample_id = fields.Many2one(comodel_name='hr.hospital.type.of.sample')
    conclusion = fields.Text()
    diagnosis_ids = fields.Many2many(comodel_name='hr.hospital.diagnosis',
                                relation='hr_hospital_research_diagnosis',
                                column1='diagnosis',
                                column2='research',
                                index=True)
    
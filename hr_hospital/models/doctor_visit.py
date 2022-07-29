from odoo import models, fields


class HrHospitalDoctorVisit(models.Model):
    _name = 'hr.hospital.doctor.visit'
    _description = "Doctor's visit"
    active = fields.Boolean(default=True)
    name = fields.Char()
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True,
                                index=True, )
    visit_date = fields.Datetime(defoult=fields.Date.today, )
    diagnosis_id = fields.Many2one(comodel_name='hr.hospital.diagnosis',
                                   index=True)
    research = fields.Many2many(comodel_name='hr.hospital.research')
    recomendation = fields.Text()
   
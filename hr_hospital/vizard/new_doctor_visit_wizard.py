from odoo import models, fields


class HrHospitalNewDoctoeVisit(models.TransientModel):
    _name = 'hr.hospital.new.doctor.visit.vizard'
    _description = 'New doctor visit'
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient',
                                 required=True)
    visit_date = fields.Datetime(default=fields.Date.today,
                             required=True)

    def new_doctor_visit(self):
        for record in self:
            self.env['hr.hospital.doctor.visit'].create({
                'doctor_id': record.doctor_id.id,
                'patient_id': record.patient_id.id,
                'visit_date': record.visit_date,        
            })  
           

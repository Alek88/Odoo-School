from odoo import models, fields


class HrHospitalAddingDoctorVizard(models.TransientModel):
    _name = 'hr.hospital.adding.doctor.vizard'
    _description = "Adding doctors for the patients"
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', string='Doctor')
    patient_ids = fields.Many2many(comodel_name='hr.hospital.patient', string='Patients')
    
    def action_adding_model(self):
        for patient_id in self.patient_ids:
            patient_id.doctor_id = self.doctor_id
        return {}    
    
    
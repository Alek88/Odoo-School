from typing_extensions import Required
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrHospitalDiagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = "Diagnosis"
    active = fields.Boolean(default=True)
    name = fields.Char(string='Diagnosis', 
                       required=True)
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor', 
                                string='Doctor',
                                required=True, 
                                index=True)
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient', 
                                 required=True, 
                                 index=True)
    res_ids = fields.Many2many(comodel_name='hr.hospital.research', 
                                    relation='hr_hospital_research_diagnosis',
                                    column1='research',
                                    column2='diagnosis',
                                    string = "Researches")
    disease_ids = fields.Many2many(comodel_name='hr.hospital.disease', 
                              index=True)
    treatment = fields.Text()
    diagnisis_date = fields.Date(string='Diagnisis date', 
                                 default=fields.Date.today, 
                                 required=True)
    
    comment = fields.Text(size=200)
    
    @api.constrains('doctor_id')
    def checking_if_doctor_is_intern(self):
        if self.doctor_id.is_intern and not self.comment:
            raise ValidationError("The comment must be filled.")

 
    
    

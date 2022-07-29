from email.policy import default
from odoo import models, fields, api


class HrHospitalDiseaseReportVizard(models.TransientModel):
    _name = 'hr.hospital.disease.report.vizard'
    _description = "Disease report vizard"
    report_date = fields.Date(string='Date')
    
    def add_disease(self):
        disease_list = self.env['hr.hospital.disease'].search([])
        if disease_list: 
            return disease_list
        return 
    
    disease_id = fields.Many2many(comodel_name='hr.hospital.disease',
                                default=add_disease)
    
    def calculate_disease(self):
        return
    
#.... і якось далі, поки що не до кінця розібрався 

    
        
        
     
 
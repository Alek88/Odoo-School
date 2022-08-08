from odoo import api, models, fields, api
from odoo.exceptions import ValidationError


class HrHospitalDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'
    _inherit = ['hr.hospital.person',] 
    active = fields.Boolean(default=True)
    speciality = fields.Char()
    is_intern = fields.Boolean()
    hospital = fields.Many2one(comodel_name='hr.hospital',
                               required=True)
    mentor_id=fields.Many2one(comodel_name='hr.hospital.doctor',
                              string='Mentor',      
                              domain=[('is_intern', '=', False)])
    
    intern_ids=fields.One2many(comodel_name='hr.hospital.doctor',
                              string='Interns',
                              inverse_name='mentor_id',   
                              domain=[('is_intern', '=', True)])
    
    patient_ids = fields.One2many(comodel_name='hr.hospital.patient',
                                  inverse_name='doctor_id')
    activity_history = fields.Text(string='Activity history')                            
                               
    @api.constrains('mentor_id')
    def cheking_mentor_id(self):
        for record in self:
            if self.id == record.mentor_id.id: 
                raise ValidationError("A doctor cannot be a mentor for himself.")
                return    
            if record.is_intern:
                if not record.mentor_id:
                    raise ValidationError("For an intern, it is necessary to specify a mentor.")  
            return

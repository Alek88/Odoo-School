from webbrowser import get
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

class HrHospitalPatient(models.Model):
    _name = 'hr.hospital.patient'
    _inherit = ['hr.hospital.person',]
    _description = 'Patient'
    active = fields.Boolean(default=True)
    birthday_date = fields.Date(string='Birthday', 
                                default=fields.Date.today,
                                required=True)
    age = fields.Integer(compute='_calculate_age', 
                         readonly=True)
    pasport_series = fields.Char(size=2)
    pasport_number = fields.Char(size=10)
    pasport_issued_date = fields.Date(string='Pasport issued date')
    pasport_issued_by = fields.Date(string='Pasport issued by')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)

    @api.depends('birthday_date')
    def _calculate_age(self):
        for record in self:
            today = fields.date.today()
            if record.birthday_date:
                record.age = relativedelta(today, record.birthday_date).years
            else:
                record.age = 0
                
    @api.model
    def create(self, vals):
        new_record = super().create(vals)
        if 'doctor_id' in vals:
            self.env['hr.hospital.pers.doc.history'].create({
                'date': fields.date.today(),
                'patient_id': new_record.id,
                'doctor_id': vals.get('doctor_id'),        
            })
            return new_record
    
    def write(self, vals):
        if 'doctor_id' not in vals:
            return super().write(vals)
        for record in self:
            if record.doctor_id.id != vals.get('doctor_id'):
                self.env['hr.hospital.pers.doc.history'].create({
                    'date': fields.date.today(),
                    'patient_id': record.id,
                    'doctor_id': vals.get('doctor_id'),        
                })
            super().write(vals) 
        return True
    
    def _get_patient_disease(self, doc):
        for pat in self:
            diagnosis =  self.env['hr.hospital.diagnosis'].search([('doctor_id', '=', doc.id), 
                                                                ('patient_id', '=', pat.id)])    
            if diagnosis:
                return diagnosis.degree_of_morbidity 
            else:
                'other'  
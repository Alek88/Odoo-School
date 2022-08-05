from odoo import models, fields, api


class HrHospitalPatientCard(models.Model):
    _name = 'hr.hospital.patient.card'
    _description = 'Patient card'
    active = fields.Boolean(default=True)
    name = fields.Char(string='Patient card name',
                       required=True)
    disease_history_ids = fields.Many2many(comodel_name='hr.hospital.disease.history')
    partient_id = fields.Many2one(string='Patient', 
                               comodel_name='hr.hospital.patient')
    
    doctor_appointment_history_ids = fields.Many2many(
                            comodel_name='hr.hospital.pers.doc.history',
                            string="Doctor's appointment history",
                            compute='_add_doctor_history')
    
    
    
    @api.depends('partient_id')
    def _add_doctor_history(self):
        for record in self:
            if record.partient_id:
                history_list = self.env['hr.hospital.pers.doc.history'].search([('patient_id', '=', record.partient_id.id)])
                if history_list:
                    record.doctor_appointment_history_ids = history_list
                else:
                    record.doctor_appointment_history_ids = ()
            else:
                record.doctor_appointment_history_ids = ()
                       
        
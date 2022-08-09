from odoo import models, fields, api


class HrHospital(models.Model):
    _name = 'hr.hospital'
    _description = 'Hospital'
    name = fields.Char(string='Hospital name',
                       required=True)
    
    logo = fields.Image(max_width=64, max_height=64)
 
            
    
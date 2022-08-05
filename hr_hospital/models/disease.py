from xml.dom import ValidationErr
from odoo import _, models, fields, api
from odoo.exceptions import ValidationError


class HrHospitalDisease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease'
    _parent_name = 'parent_id'
    _parent_store = True
    active = fields.Boolean(default=True)
    name = fields.Char(string='Disease')
    
    parent_id = fields.Many2one('hr.hospital.disease', 
                                'Parent disease', 
                                index = True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    chield_ids = fields.One2many('hr.hospital.disease', 
                                 'parent_id', 
                                 'Child disease')

    
    
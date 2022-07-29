from email.policy import default
from odoo import models, fields, _


class HrHospitalPerson(models.AbstractModel):
    _name = 'hr.hospital.person'
    _description = 'Person data' 
    active = fields.Boolean(default=True)
    name = fields.Char(string='Full name', 
                       required=True)
    phone = fields.Char(required=True)
    email = fields.Char(required=True)
    photo = fields.Image()
    gender = fields.Selection([('male', _('Male')), 
                               ('female', _('Female')),
                               ('other', _('Other'))], 
                              required=True)

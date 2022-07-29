from odoo import models, fields


class HrHospitalContactPerson(models.Model):
    _name = 'hr.hospital.contact.person'
    _description = 'Contact person'
    _inherit = 'hr.hospital.person'
    active = fields.Boolean(default=True)
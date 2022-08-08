from odoo import models, fields, api


class HrHospital(models.Model):
    _name = 'hr.hospital'
    _description = 'Hospital'
    #_inherit = 'image.mixin'
    name = fields.Char(string='Hospital name',
                       required=True)
    
    logo = fields.Image(max_width=64, max_height=64)
    #logo = fields.Image(max_width=64, max_height=64,compute='_compute_logo')

    #@api.depends('image_128')
    #def _compute_logo(self):
    #    for hosp in self:
    #       hosp.logo = hosp.image_128
            
    
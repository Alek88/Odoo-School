from odoo import _, models, fields, api
from odoo.exceptions import ValidationError


class HrHospitalTypeOfResearch(models.Model):
    _name = 'hr.hospital.type.of.research'
    _description = "Type of research" 
    _parent_name = 'parent_id'
    _parent_store = True
    active = fields.Boolean(default=True)
    name = fields.Char()
    
    parent_id = fields.Many2one('hr.hospital.type.of.research', 
                                'Type of research', 
                                index = True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    chield_ids = fields.One2many('hr.hospital.type.of.research', 
                                 'parent_id', 
                                 'Child type of research')
    
    
    @api.constrains('parent_id')
    def _chec_type_of_research_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursion catalog.'))
        return True
    
    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]
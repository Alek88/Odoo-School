from email.policy import default
from odoo import fields, models
from datetime import datetime, timedelta


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Book Authors'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date('Birthday')
    
    is_write_intern = fields.Boolean(compute='_is_allowed_to_change')
    
    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)
        
    def _is_allowed_to_change(self):
        for record in self:
            record.is_write_intern = record.create_date > datetime.now() - timedelta(days=30)   
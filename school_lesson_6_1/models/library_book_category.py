from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name='library.book.category'
    description = 'Library book category'
    name = fields.Char()
    active = fields.Boolean(default=True)


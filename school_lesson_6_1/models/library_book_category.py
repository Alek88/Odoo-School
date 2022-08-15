from odoo import models, fields


class LibraryBookCategory(models.Model):
    _name='library.book.category'
    description = 'Library book category'
    name = fields.Char()
    active = fields.Boolean(default=True)
    book_ids = fields.Many2many(comodel_name='library.book',
                                relation = 'library_book_book_category',
                                column1 = 'book_name',
                                column2 = 'category_name')

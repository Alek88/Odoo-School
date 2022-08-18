from odoo import models, fields, _


class LibraryBook(models.Model):
    _inherit = 'library.book.category'
    
    def show_books(self):
        """ The method will be called from the representation of the model form:
            library_category_views

        Returns:
            dict: method returns an action for library.book with selection 
            by category
        """
        self.ensure_one()
        return {
            'name': _('Books category'),
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'library.book',
            'domain': [('category_ids.id', '=', self.id)],
        }   
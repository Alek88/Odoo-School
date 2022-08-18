# Copyright © 2022 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'School Lesson 6 3',
    'version': '15.0.0.0.2',
    'category': 'Extra Tools',
    'summary': """
        Odoo School
        Lesson 6-3: Translating. 
    """,
    'license': 'LGPL-3',
    'author': 'Aleksander Huryn',
    'depends': [
        'school_lesson_6_2',
    ],
    'data': [
        'views/library_book_views.xml',
        'views/library_author_views.xml',
        'views/library_category_views.xml',
    ],
    'support': 'gurin.alek@gmail.com',
    'application': False,
    'installable': True,
    'auto_install': False,
}

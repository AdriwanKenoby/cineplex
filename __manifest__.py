# -*- coding: utf-8 -*-
{
    'name': "cineplex",

    'summary': """
        Gestion de salles de cinema""",

    'description': """
        salles de cinema
        seances de cinema
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/city.xml',
        'views/site.xml',
        'views/salle.xml',
        'views/seance.xml',
        'views/film.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

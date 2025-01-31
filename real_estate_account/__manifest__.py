# -*- coding: utf-8 -*-
{
    'name': "Real Estate Account",
    'summary': "link module between real estate and invoicing",
    'description': """
link module between real estate and invoicing
    """,
    'author': "Mangandaralam Sakti",
    'website': "https://github.com/Daralams/real_estate",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Property/Property',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'real_estate', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}


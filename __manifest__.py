# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': "Technical exercise with case study",
    'description': """
Technical exercise with case study
    """,
    'author': "Mangandaralam Sakti",
    'website': "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Property/Property',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menu_views.xml',
        'views/templates.xml',
    ],
    'images': ['real_estate/static/description/icon.png'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}


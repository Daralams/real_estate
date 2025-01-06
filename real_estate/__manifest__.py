# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': "The Real Estate Advertisement module",
    'description': """
The Real Estate Advertisement module
    """,
    'author': "Mangandaralam Sakti",
    'website': "https://github.com/Daralams/real_estate",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Property/Property',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_base_user_inherit_views.xml',
        # =============== sakti labs
        'views/labs/my_transient_model_view.xml',
        # =============== sakti labs
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'views/estate_property_web_template.xml',
        'views/estate_property_web_create_views.xml',
        'wizard/estate_report_excel_wizard_views.xml',
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


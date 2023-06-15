# -*- coding: utf-8 -*-
{
    'name': "Vida Product",
    'summary': """
        Support VIDA*** suite of solutions""",
    'description': """
        Supports the operations for the below operations:
        - VIDAVitamin.com
    """,
    'author': "DigiKlug Solutions LLP",
    'website': "https://www.digiklug.com/",
    'license': "Other proprietary",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product', 'account', 'base_automation'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/product.xml',
        'views/product_category.xml',
        'views/product_subscription.xml',
        'views/health_goal.xml',
        'views/partner.xml',
        'views/sale_order.xml',
        'views/settings.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "search_button",

    'summary': """
        odoo8 搜索框高级搜索按钮替换""",

    'description': """
        odoo8 搜索框高级搜索按钮替换
    """,

    'author': "JET",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/search_button.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

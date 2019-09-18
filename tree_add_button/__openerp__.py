# -*- coding: utf-8 -*-
{
    'name': "Tree视图添加按钮功能",

    'summary': """
        Tree视图添加按钮功能""",

    'description': """
        Tree视图添加按钮功能
    """,

    'author': "JET",
    'website': "https://github.com/CrazyJET",

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
        'views/tree_add_button.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

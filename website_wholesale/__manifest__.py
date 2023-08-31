# -*- coding: utf-8 -*-
{
    'name': 'Odoo Wholesale',
    'version': '16.0.1.0',
    'author': 'ERPGAP',
    'summary': 'Odoo Wholesalers Module',
    'description': """
Wholesaler
==========

This module sets a base for wholesale trade companies

- hide prices for public users

""",
    'website': 'https://www.erpgap.com',
    'category': 'Website',
    'depends': [
        'website_sale'
    ],
    'external_dependencies': [
    ],
    'data': [
        'views/website_sale_template.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

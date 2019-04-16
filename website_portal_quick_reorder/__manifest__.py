# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Quick Order (Reorder button in the Shop)',
    'version' : '1.0',
    'author': 'BulkTP, InfoTerra',
    'maintainer': 'Elsie Vernon Hogan <evhogan3@gmail.com>, Antonio Buric <antonio.burich@gmail.com>',
    'summary': 'Quick Order (Reorder)',
    'category': 'Website',
    'website': 'https://bulktoiletpaper.com/',
    'description':
        """
Quick Order (reorder) feature on the customer portal.

==========================

This module enables customers to reorder a previous order from the website and to set one order as Quick Order
which can then easily be reordered by a single click of a button under their profile data.

        """,
    'depends' : ['website_portal_sale'],
    'data': [
        'views/website_portal_sale.xml',
        'views/res_partner.xml',
    ],
    "license": "AGPL-3",
    'installable': True,
    'application': False,
    'images': ['static/description/banner.png'],
    'auto_install': False,
}

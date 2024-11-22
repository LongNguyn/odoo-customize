# -*- coding: utf-8 -*-
{
    'name': 'Purchase Son Ha',
    'version': '1.0',
    'category': 'Purchase',
    'summary': 'Son ha Purchase',
    'website': 'https://',
    'description': "Purchase Son Ha",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/x_type_budget_view.xml',
        'views/x_mch_list_view.xml',
        'views/purchase_request_view.xml',
        'views/purchase_menu.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

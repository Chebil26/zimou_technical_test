# -*- coding: utf-8 -*-
{
    'name' : 'Crm Test',
    'version' : '0.1',
    'summary' : 'Technical test',
    'description' : '',
    'depends': [
        'base',
        'sales_team',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_team_views.xml',
        'views/res_users_prospect_views.xml',
        'views/menus.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Brazilian Localisation ZIP Codes',
    'summary': 'Brazilian Localisation ZIP Codes Module used by CLVsol Solutions.',
    'version': '4.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_l10n_br_base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/l10n_br_zip_view.xml',
        'views/res_partner_view.xml',
        # 'wizard/l10n_br_zip_search_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}

# -*- coding: utf-8 -*-
# Copyright 2016, 2019 Openworx - Mario Gielissen
# Copyright 2012, 2019 Openworx - T.V.T Marine Automation
# Copyright 2019,2021 Viindoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Viindoo Backend Theme",
    "summary": "Mobile backend theme for Odoo community",
    "version": "1.0.23",

	"description": """
Backend theme for Viindoo, based on the Openworx Backend Theme

    """,

    'author': 'Openworx,T.V.T Marine Automation,Viindoo',
    'website': 'https://viindoo.com',
    'live_test_url': 'https://v13demo-int.erponline.vn',
    'support': 'apps.support@viindoo.com',

    # Categories can be used to filter modules in modules listing
    'category': 'Website/Theme/Backend',
    'version': '0.1.0',

    "depends": [
        'web',
        'web_editor',
        'web_responsive',
        'viin_brand_common',
    ],
    "data": [
    ],
    'images':[
        'images/screen.png'
    ],
    'assets':{
        'web.assets_backend': [
            ('after', '/web_responsive/static/src/legacy/scss/web_responsive.scss', '/to_backend_theme/static/src/legacy/scss/web_responsive.scss'),
            ('after', '/web_responsive/static/src/components/apps_menu/apps_menu.scss', 'to_backend_theme/static/src/scss/apps_menu.scss'),
            'to_backend_theme/static/src/scss/style.scss',
            'to_backend_theme/static/src/scss/discuss.scss',
            ],
        },
    'installable': True,
    'application': False,
    'auto_install': ['web'],
    'price': 99.9,
    'currency': 'EUR',
    'license': 'LGPL-3',
}


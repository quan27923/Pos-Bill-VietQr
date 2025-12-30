{
    'name': 'Pos Image VietQr',
    'version': '18.0.1.0.0',
    'summary': "Automatically generate VietQR QR code in POS based on bank and account number entered in configuration.",
    'author': 'Quan',
    'category': 'Point of Sale',
    'depends': ['base', 'web', 'point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'sivip_fix_report_pos/static/src/js/PosOrder.js',
            'sivip_fix_report_pos/static/src/js/payment.js',
            'sivip_fix_report_pos/static/src/xml/hide_powered_by_odoo_message.xml',         
        ],
    },
    'data': [
        'views/pos_config_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'price': 12.0,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False,
}

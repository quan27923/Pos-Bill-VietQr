{
    'name': 'Pos Bill VietQr',
    'version': '18.0.1.0.0',
    'summary': "Automatically generate VietQR QR code in POS based on bank and account number entered in configuration.",
    'author': 'Quan',
    'description': """
        The module adds the feature of creating QR payment for Point of Sale (POS).

        Main features:
        - Allows configuring QR URL in Settings.
        - Supports using variables:
        {tongtien} → Total order amount
        {noidung} → POS order code
        - When customers pay, the system automatically generates QR link based on configuration.
        - Displays QR Code directly on the POS interface and on printed invoices.
        - Does not depend on a third party, works immediately after installation.

        Suitable for:
        - Retail stores
        - Restaurants, eateries
        - Service stores
        - Point of sale that need quick QR payment

        Supports all Vietnamese banks when using VietQR link or link provided by the bank.
        
        Module thêm tính năng tạo QR thanh toán cho Điểm bán hàng (POS).

        Tính năng chính:
        - Cho phép cấu hình URL QR trong Cài đặt.
        - Hỗ trợ sử dụng các biến động:
            {tongtien}  → Tổng tiền đơn hàng
            {noidung}   → Mã đơn POS
        - Khi khách thanh toán, hệ thống tự sinh link QR dựa vào cấu hình.
        - Hiển thị QR Code trực tiếp trên giao diện POS và trên hóa đơn in.
        - Không phụ thuộc bên thứ ba, hoạt động ngay khi cài đặt.

        Phù hợp cho:
        - Cửa hàng bán lẻ
        - Quán ăn, nhà hàng
        - Cửa hàng dịch vụ
        - Điểm bán hàng cần thanh toán QR nhanh chóng

        Hỗ trợ tất cả ngân hàng Việt Nam khi dùng link VietQR hoặc link do ngân hàng cung cấp.
    """,
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
    'images': ['static/description/banner.gif'],
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
}

from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__) 

class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_payment_qr_link = fields.Char(
        string="QR thanh toán URL",
        help="Nhập link QR thanh toán, có thể dùng {tongtien} và {noidung}"
    )
    pos_bank_name = fields.Char(
        string="Ngân hàng",
        help="Tên ngân hàng sẽ hiển thị trong QR"
    )

    pos_bank_account = fields.Char(
        string="Số tài khoản",
        help="Số tài khoản sẽ hiển thị trong QR"
    )
    
    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        for order in orders:
            config = order.session_id.config_id
            order.qr_bank_name = config.pos_bank_name or ""
            order.qr_bank_account = config.pos_bank_account or ""

            if config.pos_payment_qr_link:
                total = round(order.amount_total)
                order.qr_link = config.pos_payment_qr_link.replace(
                    "{tongtien}", str(total)
                ).replace(
                    "{noidung}", order.name or ""
                )
        return orders

class PosOrder(models.Model):
    _inherit = 'pos.order'

    qr_bank_name = fields.Char(string="Ngân hàng")
    qr_bank_account = fields.Char(string="Số tài khoản")
    qr_link = fields.Char(string="QR URL")

    def _export_for_printing(self):
        res = super()._export_for_printing()
        res['qr_bank_name'] = self.qr_bank_name
        res['qr_bank_account'] = self.qr_bank_account
        res['qr_link'] = self.qr_link
        return res


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_payment_qr_link = fields.Char(
        related="pos_config_id.pos_payment_qr_link",
        readonly=False
    )
    pos_bank_name = fields.Char(
        related="pos_config_id.pos_bank_name",
        readonly=False
    )
    pos_bank_account = fields.Char(
        related="pos_config_id.pos_bank_account",
        readonly=False
    )
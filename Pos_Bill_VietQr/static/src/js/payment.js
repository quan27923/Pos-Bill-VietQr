/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

patch(PaymentScreen.prototype, {
    setup() {
        super.setup();
        const order = this.pos.get_order();
        if (order) {
            // gán từ order.pos_order (load từ backend)
            order.qr_bank_name = order.qr_bank_name || this.pos.config.pos_bank_name || "";
            // order.qr_bank_account = order.qr_bank_account || this.pos.config.pos_bank_account || "";
        }
    }
});

import { patch } from "@web/core/utils/patch";
import { PosOrder } from "@point_of_sale/app/models/pos_order";

patch(PosOrder.prototype, {
    export_for_printing() {
        const receipt = super.export_for_printing(...arguments);

        receipt.order = receipt.order || {};
        receipt.pos_bank_name = this.qr_bank_name || "";
        // receipt.pos_bank_account = this.qr_bank_account || "";
        return receipt;
    },
});

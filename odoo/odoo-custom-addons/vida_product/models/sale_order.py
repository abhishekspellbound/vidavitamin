# -*- coding: utf-8 -*-
from odoo import models, fields, api

import requests


class SaleOrder(models.Model):
    _inherit = "sale.order"

    stripe_subscription_id = fields.Char(string="Stripe Subscription Id")
    subscription_id = fields.Many2one("vida_product.product_subscription", string="Subscription", ondelete="set null", index=True)
    payment_status = fields.Char(string="Payment Status")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        url = self.env['ir.config_parameter'].get_param('vida_product.api_base_url')
        reset_subscription = self.env['ir.config_parameter'].get_param('vida_product.force_subscription_reset') or False
        if reset_subscription:
            reset_subscription = 1
        else:
            reset_subscription = 0

        if url:
            requests.get(
                url="{}api/v1/charge-order-on-stripe".format(url),
                params={"odoo_order_id": self.id, "reset_subscription": reset_subscription},
            )


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    stripe_product_id = fields.Char(string="Stripe Product Id")
    stripe_price_id = fields.Char(string="Stripe Price Id")

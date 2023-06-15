# -*- coding: utf-8 -*-
from odoo import models, fields, api

from datetime import timedelta, date, datetime
import requests


class ProductSubscription(models.Model):
    _name = "vida_product.product_subscription"
    _description = "Vida Product Subscription"

    @api.depends('customer')
    def compute_name(self):
        if self.customer.name is None:
            self.name = "New Subscription"

        self.name = "Subscription for {}".format(self.customer.name)

    customer = fields.Many2one("res.partner", string="Customer")
    name = fields.Char(string="Subscription", compute=compute_name, store=True)
    stripe_customer_id = fields.Char(string="Stripe Customer Id")
    stripe_subscription_id = fields.Char(string="Stripe Subscription Id")
    created_date = fields.Datetime(string="Created Date")
    prev_cycle_date = fields.Date(string="Previous Cycle Date")
    next_cycle_date = fields.Date(string="Next Cycle Date")
    products = fields.Many2many("product.template", string="Products")
    orders = fields.One2many("sale.order", "subscription_id", string="Orders")

    def create_order(self):
        print("Creating Order for Subscription: {}, Prev Date: {}, Next Date: {}".format(
            self.name, self.prev_cycle_date, self.next_cycle_date))

        url = self.env['ir.config_parameter'].get_param('vida_product.api_base_url')
        subscription_length = int(self.env['ir.config_parameter'].get_param('vida_product.subscription_days') or 2)
        next_two_days = datetime.now().date() + timedelta(days=subscription_length)

        if self.next_cycle_date is not None and self.next_cycle_date < next_two_days:
            if url:
                response = requests.get(
                    url="{}api/v1/create-subscription-order".format(url),
                    params={"odoo_subscription_id": self.id},
                )
                if response:
                    self.update({
                        'prev_cycle_date': self.next_cycle_date,
                        'next_cycle_date': self.next_cycle_date + timedelta(days=30),
                    })

        print("Creating Order for Subscription: {}, Prev Date: {}, Next Date: {}".format(
            self.name, self.prev_cycle_date, self.next_cycle_date))

    def trigger_cron(self):
        subscriptions = self.env["vida_product.product_subscription"].search([])

        for subscription in subscriptions:
            subscription.create_order()

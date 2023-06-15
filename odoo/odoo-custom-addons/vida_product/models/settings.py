from odoo import models, fields, api


class VidaProductSettings(models.TransientModel):
    _inherit = "res.config.settings"

    api_base_url = fields.Char(string="VIDA API Base URL", config_parameter='vida_product.api_base_url')
    subscription_days = fields.Char(
        string="Subscription Buffer (days)",
        config_parameter='vida_product.subscription_days')
    force_subscription_reset = fields.Boolean(
        string="Force Subscription Reset",
        config_parameter='vida_product.force_subscription_reset')

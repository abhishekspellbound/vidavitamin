# -*- coding: utf-8 -*-

from odoo import models, fields, api

import requests


class HealthGoal(models.Model):
    _name = "vida_product.health_goal"
    _description = "Vida Health Goal"

    name = fields.Char(string="Name")
    short_description_en = fields.Char(string="Short Description")
    short_description_ar = fields.Char(string="Short Description")
    long_description_en = fields.Text(string="Long Description")
    long_description_ar = fields.Text(string="Long Description")
    icon = fields.Char(string="Icon")
    products = fields.Many2many("product.template", string="Associated Products")

    # @api.onchange('name', 'short_description_en', 'short_description_ar', 'long_description_en', 'long_description_ar', 'icon')
    # def _health_goal_changed(self):
    #     requests.get("http://localhost:8888/test-odoo-webhook?msg=Test%20Daanish%20From%20Odoo")

    # @api.multi
    def x_health_goal_changed(self):
        requests.get("http://localhost:8888/test-odoo-webhook?msg=Test%20Daanish%20From%20Odoo%20" + self.name)

    def x_health_goal_changed_2(self):
        requests.get("http://localhost:8888/test-odoo-webhook?msg=Test%20Daanish%20From%20Odoo_2%20" + self.name)

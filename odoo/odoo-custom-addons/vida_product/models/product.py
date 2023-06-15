# -*- coding: utf-8 -*-

from odoo import models, fields, api

import requests


class Product(models.Model):
    _inherit = "product.template"

    product_id = fields.Char(string="Product Id")
    # name_en = fields.Char(string="SKU")
    # name_ar = fields.Char(string="SKU")
    medical_name = fields.Char(string="Medical Name")
    dosage = fields.Char(string="Dosage")
    stripe_product_id = fields.Char(string="Stripe Product Id")
    stripe_price_id = fields.Char(string="Stripe Price Id")
    icon = fields.Char(string="Icon")
    image = fields.Char(string="Image")
    hero_image = fields.Char(string="Hero Image")
    is_non_gmo = fields.Boolean(string="Non GMO")
    is_gluten_free = fields.Boolean(string="Gluten Free")
    is_vegan = fields.Boolean(string="Vegan")
    is_vegetarian = fields.Boolean(string="Vegetarian")
    tagline_en = fields.Char(string="Tagline")
    tagline_ar = fields.Char(string="Tagline")
    description_line_1_en = fields.Char(string="Bullet Point 1")
    description_line_2_en = fields.Char(string="Bullet Point 2")
    description_line_3_en = fields.Char(string="Bullet Point 3")
    description_line_4_en = fields.Char(string="Bullet Point 4")
    description_line_1_ar = fields.Char(string="Bullet Point 1")
    description_line_2_ar = fields.Char(string="Bullet Point 2")
    description_line_3_ar = fields.Char(string="Bullet Point 3")
    description_line_4_ar = fields.Char(string="Bullet Point 4")
    description_en = fields.Text(string="English")
    description_ar = fields.Text(string="Arabic")
    suggested_use_en = fields.Char(string="Suggested Use")
    suggested_use_ar = fields.Char(string="Suggested Use")
    ingredients_en = fields.Char(string="Ingredients")
    ingredients_ar = fields.Char(string="Ingredients")
    benefits_en = fields.Char(string="Benefits")
    benefits_ar = fields.Char(string="Benefits")
    category_id = fields.Many2one("vida_product.product_category", string="Category", ondelete="set null", index=True)
    health_goals = fields.Many2many("vida_product.health_goal", string="Health Goals")

    def product_changed(self):
        url = self.env['ir.config_parameter'].get_param('vida_product.api_base_url')

        if url:
            requests.get(
                url="{}api/v1/sync-product-from-odoo".format(url),
                params={"odoo_product_id": self.id},
            )

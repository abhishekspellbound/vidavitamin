# -*- coding: utf-8 -*-
import requests
from odoo import models, fields, api


class ProductCategory(models.Model):
    _name = 'vida_product.product_category'
    _description = "Vida Product Category"

    name = fields.Char(string="Category Name")
    category_id = fields.Integer(string="Category Id")
    description_en = fields.Text(string="Category Description")
    description_ar = fields.Text(string="Category Description")
    parent_category_id = fields.Integer(string="Parent Category")
    image = fields.Char(string="Image")
    child_categories = fields.One2many("vida_product.product_category", "parent_category_id", string="Child Categories")
    products = fields.One2many("product.template", "category_id", string="Products")

    def product_category_changed(self):
        print("Category Changed", self.category_id, self.name, self.description_en, self.description_ar)
        #requests.post("https://localhost:8888/test-odoo-webhook", json={'categoryId': self.category_id, 'nameEn': self.name, 'nameAr': self.name, 'descriptionEn': self.description_en, 'descriptionAr': self.description_ar, 'isActive': 1})

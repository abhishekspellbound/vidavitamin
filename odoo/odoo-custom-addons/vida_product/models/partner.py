from odoo import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"

    vida_user_id = fields.Char(string="Vida User ID")
    password_hash = fields.Char(string="Password Hash")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    email_notifications_enabled = fields.Boolean(string="Email Notifications")
    date_of_birth = fields.Date(string="Date of Birth")
    weight = fields.Integer(string="Weight")
    height = fields.Integer(string="Height")
    gender = fields.Char(string="Gender")
    stripe_customer_id = fields.Char(string="Stripe Customer Id")
    stripe_subscription_id = fields.Char(string="Stripe Subscription Id")
    facebook_ref = fields.Char(string="Facebook Reference")
    instagram_ref = fields.Char(string="Instagram Reference")
    twitter_ref = fields.Char(string="Twitter Reference")
    apple_ref = fields.Char(string="AppleID Reference")
    google_ref = fields.Char(string="Google Reference")
    openid_ref = fields.Char(string="Open Id Reference")

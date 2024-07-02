# -*- coding: utf-8 -*-
from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    is_wholesale = fields.Boolean('Is Wholesale')

    def is_wholesale_website_public_user(self):
        if self.is_wholesale and self.is_public_user():
            return False
        return True
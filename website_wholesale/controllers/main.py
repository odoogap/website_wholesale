from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.http import request


class WebsiteSaleInherit(WebsiteSale):

    @http.route()
    def cart(self, access_token=None, revive='', **post):
        """Disallow unauthenticated access to route='/shop/cart' """
        if request.website.is_wholesale and request.website.is_public_user():
            return request.redirect_query('/web/login', {'redirect': request.httprequest.full_path})
        return super().cart(**post)

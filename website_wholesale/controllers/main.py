from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http


class WebsiteSaleInherit(WebsiteSale):

    @http.route(auth="user", sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        """Disallow unauthenticated access to route='/shop/cart' """
        return super().cart(**post)

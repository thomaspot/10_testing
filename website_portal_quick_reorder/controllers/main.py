# -*- coding: utf-8 -*-
from odoo.http import request, route
from odoo.addons.website_sale.controllers.main import QueryURL, WebsiteSale


class Reorder(WebsiteSale):
    @route(["/quickorder/reorder/<model('sale.order'):order>"], type='http', auth="user", website=True)
    def reorder(self, order):

        new_order = order.sudo().copy()
        request.session['sale_last_order_id'] = new_order.id
        request.session['sale_order_id'] = new_order.id

        return request.redirect('/shop/payment/')

    @route(["/quickorder/set_quickorder/<model('sale.order'):order>"], type='http', auth="user", website=True)
    def set_quickorder(self, order):
        user = request.env['res.users'].sudo().browse(request.uid)
        partner = user.partner_id

        if partner and order:
            partner.sudo().write( {
                'quickorder_id': order.id
            })
            return request.redirect('/my/orders/')

    @route(['/quickorder/reorder_quickorder'], type='http', auth="user", website=True)
    def reorder_quickorder(self, **post):
        user = request.env['res.users'].sudo().browse(request.uid)
        partner = user.partner_id

        if partner.quickorder_id:
            new_order = partner.quickorder_id.sudo().copy()
            request.session['sale_last_order_id'] = new_order.id
            request.session['sale_order_id'] = new_order.id
            return request.redirect('/shop/payment')
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Controller(http.Controller):
    @http.route('/sale_order', type='http', auth="user", website=True)
    def sale_order(self):
        return request.render(
            'saleolder_form_demo.orders', {
                'orders': request.env['sale.order'].search([]),
            })

    
    @http.route('/sale_order/create', type='http', auth="user", website=True)
    def sale_order_create(self, **post):
        if post.get('pricelist_id'):
            pricelist_id = int(post.get('pricelist_id'))
            request.env['sale.order'].sudo().create({
                'partner_id': 1,
                'partner_invoice_id': 1,
                'partner_shipping_id': 1,
                'pricelist_id': pricelist_id,
            })
            return request.redirect('/sale_order/create?submitted=1')

        return request.render('saleolder_form_demo.order_create_form', {
            'pricelists':request.env['product.pricelist'].search([]),
            'submitted': post.get('submitted', False)
        })
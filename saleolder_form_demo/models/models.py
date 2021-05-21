# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class saleolder_form_demo(models.Model):
#     _name = 'saleolder_form_demo.saleolder_form_demo'
#     _description = 'saleolder_form_demo.saleolder_form_demo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

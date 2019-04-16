# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, exceptions, models, fields, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    quickorder_id = fields.Many2one('sale.order', string='Quick Order', ondelete='set null')

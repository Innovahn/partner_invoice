# -*- encoding: utf-8 -*-
from openerp import models, fields
class Contratocliente(models.Model):
        _inherit = 'res.partner'
        facturas_ids= fields.One2many("account.invoice","partner_id", string="Facturas", domain=[('state', '!=', 'paid'),('state', '!=', 'draft'),('state', '!=', 'cancel')])

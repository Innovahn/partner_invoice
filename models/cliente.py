# -*- encoding: utf-8 -*-
from openerp import models, fields, api
class Contratocliente(models.Model):
        _inherit = 'res.partner'
        facturas_ids= fields.One2many("account.invoice","partner_id", string="Facturas", domain=[('state', '!=', 'paid'),('state', '!=', 'draft'),('state', '!=', 'cancel')])
	monto_adeudado=fields.Float(string='Monto Adeudado', compute='_amount_due')
			
	@api.one
	def _amount_due(self):
		self.monto_adeudado= sum([x.residual for x in self.facturas_ids])
				
				
		

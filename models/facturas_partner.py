# -*- encoding: utf-8 -*-
from openerp import models, fields, api
class Facturaabono(models.Model):
        _inherit = 'account.invoice'
	importe_abonado=fields.Float(string='Importe Pagado', compute='_amount_paid')		
	due_invoice=fields.Boolean(string="Factura Vencida", default=False)       


	@api.one
	@api.depends("residual","amount_total")
	def _amount_paid(self):
		self.importe_abonado=self.amount_total-self.residual

	
			
	
		

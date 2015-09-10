
from openerp import api, models
class reporte(models.AbstractModel):
    _name = 'report.partner_invoice.report_facturas'
    @api.multi
    def render_html(self, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('partner_invoice.report_facturas')
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self,
            }
        return report_obj.render("partner_invoice.report_facturas",docargs)
      


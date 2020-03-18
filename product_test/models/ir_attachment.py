from odoo import models, fields, api, _
from odoo.exceptions import UserError

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    data = fields.Binary(string='data', compute='get_datas')
    
    # datas = fields.Binary(related='ir_attachment.datas')
    # mimetype = fields.Char(related='ir_attachment.mimetype')
    # datas_fname = fields.Char(related='ir_attachment.datas_fname')
    # url = fields.Char(related='ir_attachment.url')
    # index_content = fields.Text(related='ir_attachment.index_content')
    # res_model = fields.Char(related='ir_attachment.res_model')
    # res_field = fields.Char(related='ir_attachment.res_field')
    # res_id = fields.Integer(related='ir_attachment.res_id')
    @api.depends('datas')
    def get_datas(self):
        for item in self:
            item.data = item.datas
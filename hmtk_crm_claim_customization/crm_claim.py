# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2013 BroadTech IT Solutions.
#    (http://wwww.broadtech-innovations.com)
#    contact@boradtech-innovations.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
from openerp.tools.translate import _

class crm_claim(osv.osv):
    _inherit = 'crm.claim'
    
    _columns = {
        'apply_guarantee': fields.boolean('Apply guarantee'),
        'warehouse_receipt_date': fields.datetime('Warehouse receipt date to commercialization and production'),
        'production_receipt_date': fields.datetime('Receipt of production to marketing'),
        'customer_marketing_date': fields.datetime('Date customer marketing'),
        'equipment_model': fields.char('Equipment model', size=128),
        'equipment_series': fields.char('Equipment series', size=128),
        'equipment_received_state': fields.text('State in the equipment is received'),
        'diagnosis_area': fields.text('Diagnosis production area'),
        'replace_part_ids': fields.one2many('product.replace.line', 'claim_id', 'Parts to replace'),
    }
    
crm_claim()

class product_replace_line(osv.osv):
    _name = 'product.replace.line'
    _description = "Replace parts"
    _rec_name = 'product_id'
    
    _columns = {
        'claim_id': fields.many2one('crm.claim', 'Customer complaint', required=True),
        'product_id': fields.many2one('product.product','Part Name'),
        'product_qty' : fields.float('Quantity'),
        'product_uom': fields.many2one('product.uom', 'Product Unit of Measure'),
    }
    
    _defaults = {
        'product_qty': 1.0
    }
    
    def onchange_product_id(self, cr, uid, ids, product_id, context=None):
        if context is None:
            context = {}
        if product_id:
            product = self.pool.get('product.product').browse(cr, uid, product_id, context=context)
            res = {
                'product_uom': product.uom_id.id,
            }
            return {'value': res}
        return {}

product_replace_line()
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

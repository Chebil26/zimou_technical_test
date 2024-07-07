# -*- coding: utf-8 -*-

from odoo import fields, models


class ResRegion(models.Model):
    _name = 'res.region'
    _inherit = 'mail.thread'
    _description = 'Region'

    name = fields.Char('Region name', required=True, tracking=True)
    commercial_lead_id = fields.Many2one('res.users', 'Commercial lead', index=True, tracking=True)
    
    
class CrmTeam(models.Model):
    _inherit = 'crm.team'

    region_id = fields.Many2one('res.region', 'Region', tracking=True)
    
    def write(self, vals):
        res = super(CrmTeam, self).write(vals)
        if 'region_id' in vals:
            self.region_id.write({'commercial_lead_id': self.user_id.id})
        return res
        
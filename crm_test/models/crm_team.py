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

    team_lead_id = fields.Many2one('res.users', 'Team leader', index=True, tracking=True)
    region_id = fields.Many2one('res.region', 'Region', tracking=True)


class ResUsersProspect(models.Model):
    _name = 'res.users.prospect'
    _inherit = 'mail.thread'
    _description = 'Prospect'

    name = fields.Char('Name', required=True, tracking=True)
    date = fields.Date('Date', tracking=True)
    description = fields.Char('Description', tracking=True)
    user_id = fields.Many2one('res.users', 'User', index=True, required=True, tracking=True)
    
    state = fields.Selection([('contact', 'contact'), ('prospect', 'prospect'), ('offer', 'offer'),
                              ('sent', 'sent'), ('won', 'won'), ('lost', 'lost')],
                             string='State',)
    
    def write(self, vals):
        res = super(ResUsersProspect, self).write(vals)
        # create partner
        return res
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


class ResUsersProspect(models.Model):
    _name = 'res.users.prospect'
    _inherit = 'mail.thread'
    _description = 'Prospect'

    name = fields.Char('Name', required=True, tracking=True)
    date_created = fields.Date('Date created', tracking=True, readonly=True, default=fields.Date.today())
    date_won = fields.Date('Date won', tracking=True, readonly=True)
    date_lost = fields.Date('Date lost', tracking=True, readonly=True)
    date_sent = fields.Date('Date sent', tracking=True, readonly=True)
    date_offer = fields.Date('Date offer', tracking=True, readonly=True)
    description = fields.Char('Description', tracking=True)
    user_id = fields.Many2one('res.users', 'User', index=True, required=True, tracking=True)
    
    state = fields.Selection([('contact', 'Contact'), ('prospect', 'Prospect'), ('offer', 'Offer'),
                              ('sent', 'Sent'), ('won', 'Won'), ('lost', 'Lost')],
                             string='State')
    
    def btn_set_offer(self):
        self.ensure_one()
        self.write({
            'state': 'offer',
        })
        
    def btn_set_sent(self):
        self.ensure_one()
        self.write({
            'state': 'sent',
            'date_sent': fields.Date.today(),
        })
        
    def btn_set_won(self):
        self.ensure_one()
        self.write({
            'state': 'won',
            'date_won': fields.Date.today(),
        })
        
    def btn_set_lost(self):
        self.ensure_one()
        self.write({
            'state': 'lost',
            'date_lost': fields.Date.today(),
        })

    def write(self, vals):
        res = super(ResUsersProspect, self).write(vals)
        # create partner
        return res
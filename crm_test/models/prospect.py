# -*- coding: utf-8 -*-

from odoo import fields, models

class ResUsersProspect(models.Model):
    _name = 'res.users.prospect'
    _inherit = 'mail.thread'
    _description = 'Prospect'


    name = fields.Char('Name', required=True, tracking=True)
    email = fields.Char('Email', tracking=True)
    phone = fields.Char('Phone number', tracking=True)
    adress = fields.Char('Adress', tracking=True)
    partner_id = fields.Many2one('res.partner', 'Client', index=True, readonly=True)
    date_created = fields.Date('Date created', tracking=True, readonly=True, default=fields.Date.today())
    date_won = fields.Date('Date won', tracking=True, readonly=True)
    date_lost = fields.Date('Date lost', tracking=True, readonly=True)
    date_sent = fields.Date('Date sent', tracking=True, readonly=True)
    date_offer = fields.Date('Date offer', tracking=True, readonly=True)
    description = fields.Text('Description', tracking=True)
    user_id = fields.Many2one('res.users', 'User', index=True, required=True,
                                tracking=True, default=lambda self: self.env.user)
    
    state = fields.Selection([('contact', 'Contact'), ('prospect', 'Prospect'), ('offer', 'Offer'),
                              ('sent', 'Sent'), ('won', 'Won'), ('lost', 'Lost')],
                             string='State', default='contact')

    def btn_set_prospect(self):
        self.ensure_one()
        self.write({
            'state': 'prospect',
        })

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
        self._convert_prospect_to_partner()
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

    def _convert_prospect_to_partner_values(self):
        return {
            'prospect_id': self.id,
            'user_id': self.user_id.id,
            'team_id': self.user_id.sale_team_id.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
        }
    
    def _convert_prospect_to_partner(self):
        for record in self:
            partner = self.env['res.partner']\
                .create(record._convert_prospect_to_partner_values())
            record.write({
                'partner_id': partner.id
            })


class ResParnter(models.Model):
    _inherit = 'res.partner'

    prospect_id = fields.Many2one('res.users.prospect', readonly=True, index=True)


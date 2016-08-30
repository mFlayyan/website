# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    bio_website = fields.Text('Bio')
    github_website = fields.Char('Github')
    linkedin_website = fields.Char('Linkedin')
    twitter_website = fields.Char('Twitter')


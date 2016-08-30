# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, fields


class hr_department(models.Model):
    _inherit = 'hr.department'

    website_published = fields.Boolean(
        'Available in the website', copy=False, default=False)
    public_info = fields.Html('Public Info')

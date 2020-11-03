# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.tools.misc import format_date


class report_account_aged_partner(models.AbstractModel):
    _inherit = "account.aged.partner"
    _description = "Aged Partner Balances"
    _inherit = 'account.report'

    filter_analytic = True
    
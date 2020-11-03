# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, _, fields
from odoo.tools import float_is_zero
from odoo.tools.misc import format_date
from datetime import datetime, timedelta

class ReportPartnerLedger(models.AbstractModel):
    _inherit = "account.report"
    _inherit = "account.partner.ledger"
    _description = "Partner Ledger"

    filter_analytic = True


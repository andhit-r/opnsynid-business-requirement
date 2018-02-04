# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class StockLocationRoute(models.Model):
    _inherit = "stock.location.route"

    br_resource_selectable = fields.Boolean(
        string="Selectable on BR Resource",
    )

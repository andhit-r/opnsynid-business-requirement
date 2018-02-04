# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"

    br_resource_id = fields.Many2one(
        string="BR Resource Line",
        comodel_name="business.requirement.resource",
    )

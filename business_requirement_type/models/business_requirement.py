# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class BusinessRequirement(models.Model):
    _name = "business.requirement"
    _inherit = ["business.requirement"]

    type_id = fields.Many2one(
        string="Type",
        comodel_name="business.requirement_type",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

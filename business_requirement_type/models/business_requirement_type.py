# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class BusinessRequirementType(models.Model):
    _name = "business.requirement_type"
    _inherit = ["mail.thread"]
    _description = "Business Requirement Type"

    name = fields.Char(
        string="Business Requirement Type",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )

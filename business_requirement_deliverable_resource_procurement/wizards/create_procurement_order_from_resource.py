# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class CreateProcurementOrderFromResource(models.TransientModel):
    _name = "business.create_procurement_order_from_resource"
    _description = "Create Procurement Order From Resource Lines"

    @api.model
    def _default_resource_line_ids(self):
        return [(6, 0, self._context.get("active_ids", []))]

    resource_line_ids = fields.Many2many(
        string="Resource Lines",
        comodel_name="business.requirement.resource",
        relation="rel_create_procurement_2_resource",
        column1="wizard_id",
        column2="resource_id",
        default=lambda self: self._default_resource_line_ids(),
    )

    @api.multi
    def action_create_procurement_order(self):
        self.ensure_one()
        self.resource_line_ids.action_create_procurement_order()

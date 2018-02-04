# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class BusinessRequirementResource(models.Model):
    _inherit = "business.requirement.resource"

    warehouse_id = fields.Many2one(
        string="Warehouse",
        comodel_name="stock.warehouse",
    )
    location_id = fields.Many2one(
        string="Procurement Location",
        comodel_name="stock.location",
    )
    route_id = fields.Many2one(
        string="Route",
        comodel_name="stock.location.route",
        domain=[
            ("br_resource_selectable", "=", True),
        ],
    )
    date_planned = fields.Datetime(
        string="Date Planned",
    )
    procurement_id = fields.Many2one(
        string="Procurement",
        comodel_name="procurement.order",
    )

    @api.multi
    def action_create_procurement_order(self):
        for resource in self:
            if resource._check_create_procurement_order():
                resource._create_procurement_order()

    @api.multi
    def _check_create_procurement_order(self):
        self.ensure_one()
        result = True
        if self.procurement_id:
            result = False
        return result

    @api.multi
    def _create_procurement_order(self):
        self.ensure_one()
        obj_proc = self.env["procurement.order"]
        proc = obj_proc.create(self._prepare_procurement_data())
        proc.run()
        self.write({
            "procurement_id": proc.id,
        })

    @api.multi
    def _prepare_procurement_data(self):
        self.ensure_one()
        data = {
            "name": self.name,
            "origin": self.business_requirement_id.name,
            "company_id": self.env.user.company_id.id,
            "date_planned": self.date_planned,
            "product_id": self.product_id.id,
            "product_qty": self.qty,
            "product_uom": self.uom_id.id,
            "warehouse_id": self.warehouse_id.id,
            "location_id": self.location_id.id,
            "br_resource_id": self.id,
        }
        if self.route_id:
            data.update({
                "route_ids": [(6, 0, [self.route_id.id])],
            })
        return data

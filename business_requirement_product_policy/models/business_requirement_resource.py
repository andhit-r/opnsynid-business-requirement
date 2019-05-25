# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class BusinessRequirementResource(models.Model):
    _inherit = "business.requirement.resource"

    @api.multi
    @api.depends(
        "business_requirement_deliverable_id",
    )
    def _compute_resource_product(self):
        obj_product = self.env["product.template"]
        default_products = obj_product.search([])
        for resource in self:
            allowed_resource_product_template_ids = \
                allowed_resource_product_category_ids = []

            prod = resource.business_requirement_deliverable_id.product_id

            if prod and prod.restrict_resource_product:
                allowed_resource_product_template_ids = \
                    prod.allowed_resource_product_ids.ids
                allowed_resource_product_category_ids = \
                    prod.allowed_resource_product_category_ids.ids
            elif prod and not prod.restrict_resource_product:
                allowed_resource_product_template_ids = \
                    default_products.ids

            resource.allowed_resource_product_template_ids = \
                allowed_resource_product_template_ids
            resource.allowed_resource_product_category_ids = \
                allowed_resource_product_category_ids

    allowed_resource_product_template_ids = fields.Many2many(
        string="Allowed Resource Products",
        comodel_name="product.template",
        compute="_compute_resource_product",
        store=False,
    )
    allowed_resource_product_category_ids = fields.Many2many(
        string="Allowed Resource Product Categories",
        comodel_name="product.category",
        compute="_compute_resource_product",
        store=False,
    )

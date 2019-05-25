# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class BusinessRequirementDeliverable(models.Model):
    _inherit = "business.requirement.deliverable"

    @api.multi
    @api.depends(
        "business_requirement_id",
    )
    def _compute_deliverable_product(self):
        obj_product = self.env["product.product"]
        default_products = obj_product.search([])
        for deliverable in self:
            allowed_deliverable_product_ids = \
                allowed_deliverable_product_category_ids = []

            br = deliverable.business_requirement_id

            if br and br.type_id and br.type_id.restrict_deliverable_product:
                br_type = br.type_id
                allowed_deliverable_product_ids = \
                    br_type.allowed_deliverable_product_ids.ids
                allowed_deliverable_product_category_ids = \
                    br_type.allowed_deliverable_product_category_ids.ids
            elif br and br.type_id and \
                    not br.type_id.restrict_deliverable_product:
                allowed_deliverable_product_ids = \
                    default_products.ids

            deliverable.allowed_deliverable_product_ids = \
                allowed_deliverable_product_ids
            deliverable.allowed_deliverable_product_category_ids = \
                allowed_deliverable_product_category_ids

    @api.multi
    @api.depends(
        "product_id",
    )
    def _compute_resource_product(self):
        obj_product = self.env["product.template"]
        default_products = obj_product.search([])
        for deliverable in self:
            allowed_resource_product_template_ids = \
                allowed_resource_product_category_ids = []

            prod = deliverable.product_id

            if prod and prod.restrict_resource_product:
                allowed_resource_product_template_ids = \
                    prod.allowed_resource_product_ids.ids
                allowed_resource_product_category_ids = \
                    prod.allowed_resource_product_category_ids.ids
            elif prod and not prod.restrict_resource_product:
                allowed_resource_product_template_ids = \
                    default_products.ids

            deliverable.allowed_resource_product_template_ids = \
                allowed_resource_product_template_ids
            deliverable.allowed_resource_product_category_ids = \
                allowed_resource_product_category_ids

    allowed_deliverable_product_ids = fields.Many2many(
        string="Allowed Deliverable Products",
        comodel_name="product.product",
        compute="_compute_deliverable_product",
        store=False,
    )
    allowed_deliverable_product_category_ids = fields.Many2many(
        string="Allowed Deliverable Product Categories",
        comodel_name="product.category",
        compute="_compute_deliverable_product",
        store=False,
    )
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

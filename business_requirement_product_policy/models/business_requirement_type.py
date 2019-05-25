# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class BusinessRequirementType(models.Model):
    _inherit = "business.requirement_type"

    restrict_deliverable_product = fields.Boolean(
        string="Restrict Deliverable Product",
    )
    allowed_deliverable_product_ids = fields.Many2many(
        string="Allowed Deliverable Products",
        comodel_name="product.product",
        relation="rel_br_type_2_deliverable_product",
        column1="business_requirement_type_id",
        column2="product_id",
    )
    allowed_deliverable_product_category_ids = fields.Many2many(
        string="Allowed Deliverable Product Categories",
        comodel_name="product.category",
        relation="rel_br_type_2_deliverable_product_categ",
        column1="business_requirement_type_id",
        column2="product_categ_id",
    )

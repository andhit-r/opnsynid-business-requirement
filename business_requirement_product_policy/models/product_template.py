# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    restrict_resource_product = fields.Boolean(
        string="Restrict Resource Products",
    )
    allowed_resource_product_ids = fields.Many2many(
        string="Allowed Resource Products",
        comodel_name="product.template",
        relation="rel_product_tmpl_2_resource_product_tmpl",
        column1="product_tmpl_id",
        column2="resource_product_tmpl_id",
    )
    allowed_resource_product_category_ids = fields.Many2many(
        string="Allowed Resource Product Categories",
        comodel_name="product.category",
        relation="rel_product_tmpl_2_resource_product_categ",
        column1="product_tmpl_id",
        column2="product_categ_id",
    )

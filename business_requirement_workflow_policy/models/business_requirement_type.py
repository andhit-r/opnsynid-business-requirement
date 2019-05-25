# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class BusinessRequirementType(models.Model):
    _inherit = "business.requirement_type"

    br_confirm_grp_ids = fields.Many2many(
        string="Allowed To Confirm Business Requirement",
        comodel_name="res.groups",
        relation="rel_br_type_2_group_br_confirm",
        column1="business_requirement_type_id",
        column2="group_id",
    )
    br_approve_grp_ids = fields.Many2many(
        string="Allowed To Approve Business Requirement",
        comodel_name="res.groups",
        relation="rel_br_type_2_group_br_approve",
        column1="business_requirement_type_id",
        column2="group_id",
    )
    br_start_grp_ids = fields.Many2many(
        string="Allowed To Start Business Requirement",
        comodel_name="res.groups",
        relation="rel_br_type_2_group_br_start",
        column1="business_requirement_type_id",
        column2="group_id",
    )
    br_finish_grp_ids = fields.Many2many(
        string="Allowed To Finish Business Requirement",
        comodel_name="res.groups",
        relation="rel_br_type_2_group_br_finish",
        column1="business_requirement_type_id",
        column2="group_id",
    )
    br_cancel_grp_ids = fields.Many2many(
        string="Allowed To Cancel Business Requirement",
        comodel_name="res.groups",
        relation="rel_br_type_2_group_br_cancel",
        column1="business_requirement_type_id",
        column2="group_id",
    )
    br_drop_grp_ids = fields.Many2many(
        string="Allowed To Drop Business Requirement",
        comodel_name="res.groups",
        relation="rel_br_type_2_group_br_drop",
        column1="business_requirement_type_id",
        column2="group_id",
    )
    br_restart_grp_ids = fields.Many2many(
        string="Allowed To Restart Business Requirement",
        comodel_name="res.groups",
        relation="rel_br_type_2_group_br_restart",
        column1="business_requirement_type_id",
        column2="group_id",
    )

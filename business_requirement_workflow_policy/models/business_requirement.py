# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class BusinessRequirement(models.Model):
    _name = "business.requirement"
    _inherit = [
        "business.requirement",
        "base.workflow_policy_object",
    ]

    confirm_ok = fields.Boolean(
        string="Can Confirm",
        compute="_compute_policy",
    )
    approve_ok = fields.Boolean(
        string="Can Approve",
        compute="_compute_policy",
    )
    start_ok = fields.Boolean(
        string="Can Start",
        compute="_compute_policy",
    )
    finish_ok = fields.Boolean(
        string="Can Finish",
        compute="_compute_policy",
    )
    drop_ok = fields.Boolean(
        string="Can Drop",
        compute="_compute_policy",
    )
    cancel_ok = fields.Boolean(
        string="Can Cancel",
        compute="_compute_policy",
    )
    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
    )

    @api.multi
    def action_confirm(self):
        for br in self:
            br.write(br._prepare_confirm_data())

    @api.multi
    def action_approve(self):
        for br in self:
            br.write(br._prepare_approve_data())

    @api.multi
    def action_start(self):
        for br in self:
            br.write(br._prepare_start_data())

    @api.multi
    def action_finish(self):
        for br in self:
            br.write(br._prepare_finish_data())

    @api.multi
    def action_drop(self):
        for br in self:
            br.write(br._prepare_drop_data())

    @api.multi
    def action_cancel(self):
        for br in self:
            br.write(br._prepare_cancel_data())

    @api.multi
    def action_restart(self):
        for br in self:
            br.write(br._prepare_restart_data())

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        return {
            "state": "confirmed",
        }

    @api.multi
    def _prepare_approve_data(self):
        self.ensure_one()
        return {
            "state": "stakeholder_approval",
        }

    @api.multi
    def _prepare_start_data(self):
        self.ensure_one()
        return {
            "state": "in_progress",
        }

    @api.multi
    def _prepare_finish_data(self):
        self.ensure_one()
        return {
            "state": "done",
        }

    @api.multi
    def _prepare_drop_data(self):
        self.ensure_one()
        return {
            "state": "drop",
        }

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        return {
            "state": "cancel",
        }

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        return {
            "state": "draft",
        }

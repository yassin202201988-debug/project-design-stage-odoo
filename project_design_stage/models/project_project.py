from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    design_stage = fields.Selection([
        ('concept', 'Concept'),
        ('draft', 'Draft'),
        ('client_review', 'Client Review'),
        ('approved', 'Approved'),
    ], string='Design Stage', default='concept', tracking=True)

    design_checklist_ids = fields.One2many(
        'project.design.checklist.item', 'project_id', string='Design Checklist')

    design_checklist_done_count = fields.Integer(
        string='Completed Items', compute='_compute_design_checklist_progress')
    design_checklist_total_count = fields.Integer(
        string='Total Items', compute='_compute_design_checklist_progress')

    design_budget_line_ids = fields.One2many(
        'project.design.budget.line', 'project_id', string='Design Budget Lines')

    total_planned_budget = fields.Monetary(
        string='Total Planned Budget',
        compute='_compute_total_planned_budget',
        currency_field='currency_id')

    currency_id = fields.Many2one(
        related='company_id.currency_id', store=True, readonly=True)

    @api.depends('design_checklist_ids.is_done')
    def _compute_design_checklist_progress(self):
        for project in self:
            items = project.design_checklist_ids
            project.design_checklist_total_count = len(items)
            project.design_checklist_done_count = len(items.filtered('is_done'))

    @api.depends('design_budget_line_ids.planned_amount')
    def _compute_total_planned_budget(self):
        for project in self:
            project.total_planned_budget = sum(
                project.design_budget_line_ids.mapped('planned_amount'))

    def action_view_design_stage(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Design Stage',
            'res_model': 'project.project',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }

    def action_view_checklist(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Design Checklist',
            'res_model': 'project.design.checklist.item',
            'view_mode': 'tree,form',
            'domain': [('project_id', '=', self.id)],
            'context': {'default_project_id': self.id},
        }
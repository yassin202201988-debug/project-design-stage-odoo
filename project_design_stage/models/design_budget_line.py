from odoo import api, fields, models


class ProjectDesignBudgetLine(models.Model):
    _name = 'project.design.budget.line'
    _description = 'Design Stage Budget Line'

    project_id = fields.Many2one(
        'project.project', string='Project', required=True, ondelete='cascade')
    design_stage = fields.Selection([
        ('concept', 'Concept'),
        ('draft', 'Draft'),
        ('client_review', 'Client Review'),
        ('approved', 'Approved'),
    ], string='Design Stage', required=True)
    planned_amount = fields.Monetary(string='Planned Budget')
    currency_id = fields.Many2one(
        related='project_id.currency_id', store=True, readonly=True)
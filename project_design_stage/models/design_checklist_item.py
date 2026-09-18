from odoo import fields, models


class ProjectDesignChecklistItem(models.Model):
    _name = 'project.design.checklist.item'
    _description = 'Design Stage Checklist Item'
    _order = 'sequence, id'

    project_id = fields.Many2one('project.project', string='Project', required=True, ondelete='cascade')
    sequence = fields.Integer(default=10)
    name = fields.Char(string='Requirement', required=True)
    stage = fields.Selection([
        ('concept', 'Concept'),
        ('draft', 'Draft'),
        ('client_review', 'Client Review'),
        ('approved', 'Approved'),
    ], string='Design Stage', required=True)
    is_done = fields.Boolean(string='Done')
    attachment_id = fields.Many2one('ir.attachment', string='Attachment')
    note = fields.Char(string='Note')
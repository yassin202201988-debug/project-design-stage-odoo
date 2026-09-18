{
    'name': 'Project Design Stage',
    'version': '17.0.1.0.0',
    'summary': 'Adds a design stage workflow to Projects for architecture/engineering',
    'category': 'Project',
    'depends': ['project', 'mail'],
    'data': [
        'security/design_security.xml',
        'security/ir.model.access.csv',
        'views/project_project_views.xml',
        'views/portal_templates.xml',
        'reports/project_design_stage_report.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
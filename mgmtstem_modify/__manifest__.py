# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Management System - Audit Modified",
    "version": "16.0.1.0.1",
    "author": "Akshat Gupta",
    "category": "Management System",
    "depends": ["mgmtsystem_audit", 'hr','mgmtsystem','mgmtsystem_action','mgmtsystem_nonconformity','document_page','mail'],
    "data": [
        'security/ir.model.access.csv',
        'data/audit_sequence.xml',
        'data/ir_cron.xml',
        'data/audit_target_mail_template.xml',
        'views/new_menus_mgmtsys.xml',
        'views/new_sections_for_audit_view.xml',
        'views/employee_view_inherit.xml',
        "views/mgmtsystem_verification_changes.xml",
        'views/audit_module_addons_view.xml',
        'views/auditors_view.xml',
        'views/mgmtsystem_nonconformity_view_inherit.xml',
        'views/auditee_view_in_audit.xml',
        'views/audit_n_auditor_screen_stages.xml',
        'views/audit_mailing_view.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}

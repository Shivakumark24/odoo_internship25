{
    'name': 'sample_module',  # Must be lowercase to match directory
    'version': '18.0.0.0',
    'summary': 'This Module for training purposes',
    'description': """This Module for training purposes.""",
    'category': '',
    'author': 'shivakumar',
    'website': 'www.zbeanztech.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/model_one_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
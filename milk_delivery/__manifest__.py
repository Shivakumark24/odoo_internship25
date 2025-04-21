{
    'name': 'Milk Delivery',
    'version': '1.0',
    'summary': 'Manage milk delivery records',
    'description': 'A module to track milk deliveries, including customer, quantity, and payment status.',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'views/milk_view.xml',
        'views/menu.xml',
        'data/ir.model.access.csv',
        'data/milk_demo.xml',
    ],
    'installable': True,
    'application': True,
}
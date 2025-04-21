from odoo import models, fields, api

class MilkDelivery(models.Model):
    _name = 'milk.delivery'
    _description = 'Milk Delivery'
    _order = 'delivery_date desc'

    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        domain=[('customer_rank', '>', 0)]
    )
    quantity_liters = fields.Float(
        string='Quantity (Liters)',
        required=True,
        digits=(12, 2)
    )
    delivery_date = fields.Date(
        string='Delivery Date',
        required=True,
        default=fields.Date.context_today
    )
    is_paid = fields.Boolean(string='Paid', default=False)
    unit_price = fields.Float(string='Price per Liter', default=1.5)
    total_amount = fields.Float(
        string='Total Amount',
        compute='_compute_total_amount',
        store=True
    )

    @api.depends('quantity_liters', 'unit_price')
    def _compute_total_amount(self):
        for delivery in self:
            delivery.total_amount = delivery.quantity_liters * delivery.unit_price
class User:
    def __init__(self, catalog):
        self.catalog = catalog

    def order_item(self, id, amount):
        item_to_order = self.catalog.get_item(id)
        #  add to order
        item_to_order.decrease_amount(amount)
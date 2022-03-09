class User:

    def __init__(self, catalog):
        self.catalog = catalog
        self.order_for_user = []

    def order_item(self, id, amount):
        item_to_order = self.catalog.add_item_to_order(id, amount)
        self.order_for_user.append(item_to_order)
        result = "\n".join([str(item) for item in self.order_for_user])
        return result

    def clear(self):
        self.order_for_user = []

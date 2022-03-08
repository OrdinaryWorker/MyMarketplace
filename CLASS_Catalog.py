from CLASS_Item import Item

class Catalog:
    def __init__(self):
        self.items_dict = {}

    def add_item(self, item_name, item_description, item_amount):
        new_item = Item(item_name, item_description, item_amount)
        item_id = new_item.get_id()
        if item_id not in self.items_dict.keys():
            self.items_dict[item_id] = new_item
        else:
            self.items_dict[item_id].increase_amount(item_amount)
        return item_id

    def list_items(self):
        return list(self.items_dict.values())

    def get_item(self, id):
        return self.items_dict[id]

import hashlib
'''
Что должен уметь магазинчик:
1. Хозяин - администратор, должен уметь, добавлять товары в каталог. То есть только у Администратора есть необходимые методы
2. Товары находятся в общем каталоге.
3. Система (Администратор) может добавлять пользователей в магазин.
4. Пользователь выбирает товар для выбора, после чего добавляет товар в корзину. После этого может может указать адрес доставки, и оплатить.
5. Система (Order) - проверяет что заказ оплачен.
'''

def hash_string(string):
    temp = str(hashlib.sha256(string.encode('utf-8')).hexdigest())
    return temp[0:10]


class Item:
    def __init__(self, item_name, description, item_count):
        self.item_id = hash_string(item_name + description)
        self.item_name = item_name
        self.description = description
        self.item_count = item_count

    def increase_amount(self, count):
        self.item_count += count

    def decrease_amount(self, count):
        self.item_count -= count

    def get_id(self):
        return self.item_id

    def __str__(self):
        return str(f'{self.item_id}, {self.item_name}, {self.description}, {self.item_count}')


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
        return item_id  # TODO remove?

    def list_items(self):
        return list(self.items_dict.values())

    def get_item(self, id):
        return self.items_dict[id]


class Administrator:

    def __init__(self, catalog):
        self.catalog = catalog

    def add_item(self, item_name, item_description, item_amount):
        self.catalog.add_item(item_name, item_description, item_amount)


class User:
    def __init__(self, catalog):
        self.catalog = catalog

    def order_item(self, id, amount):
        item_to_order = self.catalog.get_item(id)
        # TODO: add to order
        item_to_order.decrease_amount(amount)


catalog = Catalog()
admin = Administrator(catalog)
admin.add_item("gaming_mouse", "price 1000$", 5)
admin.add_item("gaming monitor", "price 10$", 55)
admin.add_item("gaming keyboard", "price 1$", 15)

item_list = catalog.list_items()
print("Before Oleg's shopping")

for item in item_list:
    print(item)

user_oleg = User(catalog)

user_oleg.order_item(item_list[0].get_id(), 2)
user_oleg.order_item(item_list[1].get_id(), 1)

print("After Oleg's shopping")
for item in item_list:
    print(item)

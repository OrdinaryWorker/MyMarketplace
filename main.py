from CLASS_Administrator import *
from CLASS_Catalog import Catalog
from CLASS_User import User
'''
Что должен уметь магазинчик:
1. Хозяин - администратор, должен уметь, добавлять товары в каталог. То есть только у Администратора есть необходимые методы
2. Товары находятся в общем каталоге.
3. Система (Администратор) может добавлять пользователей в магазин.
4. Пользователь выбирает товар для выбора, после чего добавляет товар в корзину. После этого может может указать адрес доставки, и оплатить.
5. Система (Order) - проверяет что заказ оплачен.
'''

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

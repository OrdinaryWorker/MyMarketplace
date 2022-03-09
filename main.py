from CLASS_Administrator import *
from CLASS_Catalog import Catalog
from CLASS_User import User
from data_items import data

'''
"Этот магазинчик умеет:
1. Хозяин - администратор, должен уметь, добавлять товары в каталог. 
   То есть только у Администратора есть необходимые методы
2. Товары находятся в общем каталоге.
3. Пользователь выбирает товар для выбора, после чего добавляет товар в корзину. 
'''

catalog = Catalog(data)
admin = Administrator(catalog)
admin.add_item("Rom Capitan", "200", 5)
admin.del_item('ce9da1300b')
print("Before Oleg's shopping")
catalog.print()


user_oleg = User(catalog)
print('pokupki')
print(user_oleg.order_item('18779b2d9f', 2))

print("After Oleg's shopping")
catalog.print()

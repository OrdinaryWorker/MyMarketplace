import hashlib


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
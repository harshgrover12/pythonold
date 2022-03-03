import csv


class Item:
    all = []
    pay_rate = 0.8

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name},{self.price},{self.quantity}')"

    # in class method, class itself is passed as first argument unlike object in instance method
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=item.get('quantity')
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # Count out the floats that are .0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7))  # True
print(Item.is_integer(7.0))  # True,return num.is_integer()
print(Item.is_integer(8.5))  # False


'''
When to use class method and when to use static method?

static method- This should do something that has a relationship with the class but not not something
that must be unique per instance.

class method- This should also do something that has relationship with the class but usually that are used
to manipulate structure of data to instantiate object like we we have done with CSV.
'''
# STATIC METHOD AND CLASS METHOD CAN BE CALLED FROM INSTANCE OBJECT.





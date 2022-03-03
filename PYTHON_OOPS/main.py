from PYTHON_OOPS.item import Item
from PYTHON_OOPS.phone import Phone

Item.instantiate_from_csv()
print(Item.all)

item1 = Item('MyItem', 750, 5)
item1.name = 'otheritem'  # with the help of setter, we are able to modify the item name
print(item1.name)
print(item1.read_only_name)  # its an property
# item1.read_only_name = 'BBB'  # AttributeError: can't set attribute


# In case we don't want to allow attribute modification like as done for
# item1.name, that feature is called encapsulation

print(item1.price)  # 750
item1.apply_increment(0.2)
print(item1.price)  # 900.0
'''
That is what encapsulation, not allowing attribute access/modification directly instead via getter/setter.
'''

'''
Abstraction- shows only necessary attributes and hides unnecessary details.
Adding __ in front of method means converting to private methods, abstraction can be achieved.
'''

'''
len(), function in python is perfect example for polyphormism, as according to datatype passed it
will return the result like 
len('Harsh Grover') - 12
len(['Harsh','Grover']) - 2
'''

# usage of apply_discount method in Phone class
item1 = Phone('jscphone', 1000, 3)
item1.apply_discount()
print(item1.price)
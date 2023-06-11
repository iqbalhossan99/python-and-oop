class Shop:
    shopingMall = 'Bosundara'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

    def addToCart(self, item):
        self.cart.append(item)


iqbal = Shop("Iqbal")
iqbal.addToCart("Pollo")

print(iqbal.cart)

yousuf = Shop('Yousuf')
yousuf.addToCart('Mobile')
print(yousuf.cart)


class Car:
    def __init__(self, color):
        self.color = color  # This is an instance attribute

car1 = Car("red")
car2 = Car("blue")

print(car1.color)  # Output: red
print(car2.color)  # Output: blue


"""In Python, an instance attribute is a variable that is specific to an individual instance (object) of a class. Unlike class attributes, instance attributes are unique to each instance and can have different values for different instances of the same class.

Instance attributes are defined within the methods of a class, typically within the `__init__()` method, which is a special method used to initialize the object's attributes.

Here's an example to illustrate the concept of instance attributes:

```python
class Car:
    def __init__(self, color):
        self.color = color  # This is an instance attribute

car1 = Car("red")
car2 = Car("blue")

print(car1.color)  # Output: red
print(car2.color)  # Output: blue
```

In this example, the `color` attribute is an instance attribute defined within the `__init__()` method of the `Car` class. Each instance of the class (`car1` and `car2`) has its own `color` attribute with a different value.

Instance attributes are accessed and modified using dot notation (`instance_name.attribute_name`). Each instance maintains its own set of instance attributes, and changes made to one instance's attribute do not affect other instances.

Instance attributes allow objects of the same class to have different properties or characteristics. They are particularly useful when you want each instance of a class to have its own unique state or data.

"""
class Shoping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def addToCart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
        print(self.cart)

    def remove_item(self, item):
        for productItem in self.cart:
            if item == productItem["item"]:
                self.cart.remove(productItem)
            print("product item: ", productItem["item"] )

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        
        print('Total price: ', total)

        if amount < total:
            print(f'Please provide: {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your item and extra monye {extra}')

fakhrul = Shoping('Fakhrul')

fakhrul.addToCart('Boutique', 650, 6)

fakhrul.checkout(4000)

Sabbir = Shoping('Sabbir')

Sabbir.addToCart('mom boutique', 700, 7)

Sabbir.checkout(4200)
fakhrul.remove_item("Boutique")
print(fakhrul.cart)

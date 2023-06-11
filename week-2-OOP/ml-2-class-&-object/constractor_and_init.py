class Phone:
    # this is class variable/attribute that get access And can modify of all instance of this class. 
    manufactured = "China"

    # constructor
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)


myPhone = Phone('Iqbal', 'honor', 16500)

print(myPhone.owner, myPhone.brand, myPhone.price, myPhone.manufactured)

fathersPhone = Phone("Father", 'Symphoni', 2250)
print(fathersPhone.owner, fathersPhone.brand, fathersPhone.price, fathersPhone.manufactured)
from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from User import Customer, Employee, Server, Chef, Manager
from Order import Order

"""

Pizza List:

Neapolitan Pizza.
Chicago Pizza.
New York-Style Pizza.
Sicilian Pizza.
Greek Pizza.
California Pizza.
Detroit Pizza.
St. Louis Pizza.

Burger list:

Turkey burger. ...
Portobello mushroom burger. ...
Veggie burger. ...
Wild salmon burger. ...
Bean burger. ...
Cheeseburger.

"""
def main():
    menu = Menu()
    pizza_neapolitan= Pizza("Neapolitan Pizza", 600, "large", ["Neapo", "Onion"]  )
    pizza_chicago = Pizza("Chicago Pizza", 400, "medium", ["Neapo", "Onion"]  )
    pizza_silian = Pizza("Sicilian Pizza", 500, "small", ["Neapo", "Onion"]  )
    pizza_greek = Pizza("Greek Pizza", 300, "large", ["Neapo", "Onion"]  )

    menu.add_menu_item("pizza", pizza_neapolitan)
    menu.add_menu_item("pizza", pizza_chicago)
    menu.add_menu_item("pizza", pizza_silian)
    menu.add_menu_item("pizza", pizza_greek)

    # add burger to the menu
    burger_turkey = Burger("Turkey burger", 300, "chicken", ["bread", "chili"])
    burger_portobello = Burger("Portobello burger", 300, "cow", ["bread", "chili"])
    burger_veggie = Burger("Veggie burger", 300, "vegteble", ["bread", "chili"])
    burger_wild_salmon = Burger("Wild salmon burger", 300, "chicken", ["bread", "chili"])

    menu.add_menu_item("burger", burger_turkey)
    menu.add_menu_item("burger", burger_portobello)
    menu.add_menu_item("burger", burger_veggie)
    menu.add_menu_item("burger", burger_wild_salmon)

    # add drinks to the menu
    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha Coffee', 300, False)
    menu.add_menu_item('drinks', coffee)

    # show menu
    # menu.show_menu()

    restaurant = Restaurant("Kuregor Restaurant", 2000, menu)

    # manager = Manager("Sabbir", 600, "sabbir@gmail.com", "Cumillah", 34, 15000, "Agust 1 2022", "core")
    # restaurant.add_employee("manager", manager)

    manager = Manager("Sabbir", 656, "sabbir@gmail.com", "Cumillah", 54, 15000, "01 august 2022", "Management")
    restaurant.add_employee("manager", manager)

    chef = Chef("Kuddus", 456, "kuddus@gmail.com", "Dorikila", 56, 12000, "5 September 2022", "Chef", "everything")
    restaurant.add_employee("chef", chef)

    server = Server("Karim", 4563, "karim@gmail.com", "chander dese", 89, 8000, "01 February 2022", "Waiter")
    restaurant.add_employee("server", server)

    # Customer 1 placing an order
    customer_1 = Customer("Yousuf",7869, "yousuf@gmail.com", "Chadpur", 2, 25000)
    order_1 = Order(customer_1, [pizza_chicago, coffee])
    customer_1.place_order(order_1)
    restaurant.add_order(order_1)

    # Customer one paying for order_1
    rest_money = restaurant.receive_payment(order_1, 1000, customer_1)

    print(restaurant.balance, restaurant.revenue, rest_money )




    restaurant.show_employees()
    # restaurant.add_employee("")

if __name__ == "__main__":
    main()
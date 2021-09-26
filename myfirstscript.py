import time
"""
Recommend to run this program on repl.it because I have found that importing pytz and timezones, and print(/033c) statements tend to not work, the scale of repl.it is also better for the formatting and the aesthetics of the outputted code
"""

#Menu listsgfgdf

regular_menu_list = [
    "regular hawaiian", "regular beef and onion", "regular margherita",
    "regular cheese supreme", "regular meatlovers", "regular vegetarian"
]

large_menu_list = [
    "large hawaiian ", "large beef and onion ", "large margherita ",
    "large cheese supreme ", "large meatlovers ", "large vegetarian "
]

drinks_list = ["coke", "sprite", "fanta", "lift", "pepsi"]

sides_list = ["6 chicken nuggets", "churros", "sundae", "chips"]

PRICE_LIST = [12, 18, 3, 5]  #Used to determine the prices of items


def menu():  #This function only prints the menu
    print("------------------")
    print("Pizza Planet Menu:")
    print("------------------")
    print("🍕 R̲e̲g̲u̲l̲a̲r̲ P̲i̲z̲z̲a̲s̲:̲ 🍕")
    for i in range(len(regular_menu_list)):
        print("• " + regular_menu_list[i] + " - $12")
    print()
    print("🍕 L̲a̲r̲g̲e̲ P̲i̲z̲z̲a̲s̲:̲ 🍕")
    for i in range(len(large_menu_list)):
        print("• " + large_menu_list[i] + " - $18")
    print()
    print("🥤 D̲r̲i̲n̲k̲s̲:̲ 🥤")
    for i in range(len(drinks_list)):
        print("• " + drinks_list[i] + " - $3")
    print()
    print("🍟 S̲i̲d̲e̲s̲:̲ 🍟")
    for i in range(len(sides_list)):
        print("• " + sides_list[i] + " - $5")
    print("")
    order()


def order(
):  #Asks the user to enter their order in the format | item, item, item |
    order = input("Enter your order: ").lower()
    order_list = []
    order_list += order.split(", ")
    validate_item(order_list)


def validate_item(
    order_list
):  #Checks if the items in the list are on the menu and are formatted correctly
    while True:
        for item in order_list:
            if item not in regular_menu_list and item not in large_menu_list and item not in drinks_list and item not in sides_list:  #Checks if a item is in the item lists
                print(
                    "The order item, {}, is not a valid item from the menu, please check the spelling for the item and use the format, | item, item, item, | etc"
                    .format(item))  #Tells the customer the item is not valid
                num = order_list.index(
                    item)  #Finds the location of the item in the list
                order_list.pop(
                    num)  #Removes the item using its location in the list
                print()
                new_item = input(
                    "Please enter the correct item from the menu or enter [redo] to start a new order: "
                ).lower()
                if new_item == "redo":
                    menu()
                print()
                order_list.append(
                    new_item
                )  #Adds item to list and then checks if the new item is valid by running the function again until all items are valid
                validate_item(order_list)
            else:
                break
        break
    remove_items_question(order_list)


def remove_items_question(
        order_list):  #Asks the customer if any items would like to be removed
    while True:
        answer = input(
            "Would you like to remove any items from your order? [yes] or [no]  "
        ).lower()
        if answer == "yes":
            remove_item(order_list)
        elif answer == "no":
            delivery_option(order_list)
        else:
            print("Please enter [yes] or [no]")


def remove_item(order_list):
    print("Your items are:")
    if len(order_list
           ) >= 1:  #Checks if there are any items in the customers order
        for i in range(len(order_list)):
            print(" " + str(i + 1) + ") " + order_list[i])
    else:
        print(
            "You have no items in your order"
        )  #Incase there are no items in the order it returns the customer to the ordering process
        print("Returning to order input")
        time.sleep(1.5)
        print()
        menu()
    while True:
        try:
            while True:
                try:
                    answer = int(
                        input(
                            "Enter the number of the item you would like to remove: "
                        ))
                    break
                except ValueError or answer == 0 or answer <= (
                        len(order_list)
                ):  #Input validation and checks that the number is not 0
                    print("Please enter a number from the list")
            if answer <= 0:  #If the number is 0 or less it returns the customer to the remove items question
                remove_items_question(order_list)
            order_list.pop(answer - 1)  #Removes the item from the list
            break
        except IndexError or answer == 0:  #Checks if the item is in the list and if double checks that the item number is valid
            print('Sorry that item does not exist')
            while True:
                new_answer = input(
                    "Would you still like to remove an item? [yes] or [no] "
                ).lower()
                if new_answer == "no":
                    delivery_option(order_list)
                elif new_answer != "yes" or new_answer != "no":
                    print("Please enter [yes] or [no]")
                elif new_answer == "yes":
                    break
    return order_list


def delivery_option(
        order_list
):  #Asks the customer if they would like their order delivered
    print('\033c')  #Clears everything outputted above it
    print('\x1bc')
    if len(order_list) <= 0:  #Checks that there is actually items to deliver
        print("You have no items in your order")
        print("Returning to order input")
        time.sleep(1.5)  #Gives some time before returning to the menu
        print()
        menu()
        """
			Everything below this point in this function validates the users answer, and if the answer is "delivery" it will add a $15 surcharge to the order later on and will add delivery to the order. For delivery and pickup, it gives estimated times based on time zones that are slightly ahead, or slightly a day and a bit ahead,the delivery time is slightly more than an hour ahead and the pickup time is slightly less than an hour.
		"""
    while True:
        answer = input("Would you like to [pickup] or [delivery]? ").lower()
        if answer == "pickup":
            from datetime import datetime
            import pytz
            tz_Douala = pytz.timezone(
                'Africa/Douala')  #Creates a time variable for the timezone
            pickup_datetime = datetime.now(
                tz_Douala)  #Saves the current time of the timezone as a string
            print("Your order will be availble for pickup at: ",
                  pickup_datetime.strftime("%H:%M:%S"))  #Formats the time
            delivery_option = "no"
            calculate_price(order_list, delivery_option)
        elif answer == "delivery":
            print(
                "Delivery has been added to your order, $15 charge for delivery"
            )
            from datetime import datetime
            import pytz
            tz_London = pytz.timezone(
                'Europe/London')  #Creates a time variable for the timezone
            delivery_datetime = datetime.now(
                tz_London)  #Saves the current time of the timezone as a string
            print("Your order will be delivered at:",
                  delivery_datetime.strftime("%H:%M:%S"))  #Formats the time
            delivery_option = "yes"
            calculate_price(order_list, delivery_option)
        else:
            print("Please enter [pickup] or [delivery]")


def calculate_price(
        order_list,
        delivery_option):  #Calculates the total price of the customers order
    total_price = 0
    price = 0
    for item in order_list:
        if item in regular_menu_list:  #Checks which list the item is in
            price = PRICE_LIST[
                0]  #Uses the price in PRICE_LIST as somewhat of a constant
            total_price += price  #Adds price of the item to the total price of the order
        elif item in large_menu_list:
            price = PRICE_LIST[1]
            total_price += price
        elif item in drinks_list:
            price = PRICE_LIST[2]
            total_price += price
        elif item in sides_list:
            price = PRICE_LIST[3]
            total_price += PRICE_LIST[3]
        else:
            print("Your item {} is not available or not valid".format(item))
    if delivery_option == "yes":  #Adds delivery cost
        total_price += 15
        order_list.append("Deliver Order")  #Adds delivery to the order
    payment(total_price, order_list)


def payment(total_price, order_list):
    payment_method = ""
    print()
    print("Your Order: ")  #Prints an early reciept for the customer
    print()
    for i in range(len(order_list)):
        print("• " + order_list[i])
    import datetime
    time_now = datetime.datetime.now()
    print()
    print("Total Price: ${}".format(
        total_price))  #Prints the toal price of the customers order
    print()
    print("Pizza Planet, 34 Beach Street")  #Address of the shop
    print("Date: " +
          time_now.strftime("%Y-%m-%d %H:%M:%S"))  #Current date and time
    print()
    print("-------------------------------")
    print()
    while True:  #Asks how the customer would like to pay
        payment_method = input(
            "The total price of your order is ${}, how would you like to pay?, [Cash] or [Card]? "
            .format(total_price)).lower()
        if payment_method == "card":
            card_payment(total_price, order_list, time_now)
        elif payment_method == "cash":
            cash_payment(total_price, order_list, time_now)
        else:
            print("Please enter [cash] or [card]")


def card_payment(
    total_price, order_list, time_now
):  #Simulates would it would be to order with a card, this function is for aesthetics only
    answer = input("Please enter your card number: ")
    time.sleep(1)
    answer = input("Please enter the expiry date: ")
    time.sleep(1)
    answer = input("Please enter the CVC number: ")
    time.sleep(1)
    answer = answer * 0  #Repl.it does not like having a useless variable so need to add this for the code to run
    print("Payment Successful")
    print_receipt(total_price, order_list, time_now)


def print_receipt(total_price, order_list,
                  time_now):  #Prints the final receipt for the customer
    print()
    print("-------------------------------")
    print()
    print("Your Digital Reciept:")
    print()
    print("Pizza Planet Order:")
    print()
    for i in range(len(order_list)):  #Prints the items in the order
        print("• " + order_list[i])
    print()
    print("Total Price: ${}".format(total_price))  #Prints total price
    print()
    print("Pizza Planet, 34 Beach Street"
          )  #Prints address of shop incase the user needs to pickup the order
    print("Date: " + time_now.strftime("%Y-%m-%d %H:%M:%S")
          )  #Prints the current date and time
    print()
    print("-------------------------------")
    print()
    order_again()


#Print reciept option thing before purchase


def cash_payment(total_price, order_list, time_now):
    print("Please bring your digital receipt instore to pay with cash")
    print_receipt(total_price, order_list, time_now)


def order_again():  #Asks the user if they would like to create another order
    while True:
        answer = input(
            "Would you like to create another order? [yes]/[no] ").lower()
        if answer == "yes":
            print('\033c')  #Clears all outputted text above it
            print('\x1bc')
            menu()
        elif answer == "no":
            print('\033c')
            print('\x1bc')
            end()
        else:
            print("Please enter [yes] or [no]")

def end():  #Really dum ending image

    print("""

		  ____________________________________________
		 /                                            \
 ____   < Thank you for ordering from Pizza Planet !!! |
/    \	 \____________________________________________/
  u  u|      _______
    \ |  .-''#%&#&%#``-.
   = /  ((%&#&#&%&VK&%&))
    |    `-._#%&##&%_.-'
 /\/\`--.   `-."".-'
 |  |    \   /`./
 |\/|  \  `-'  /
 || |   \     /
 	""")



#Clears everything
print('\033c')
print('\x1bc')

#Prints Logo
print("""
╭━━━━━╮                   ╭━━━━━┳━╮               ╭━╮
┃ ╭━╮ ┃                   ┃ ╭━╮ ┃ ┃              ╭╯ ╰╮
┃ ╰━╯ ┣━┳━━━━━┳━━━━━┳━━━━╮┃ ╰━╯ ┃ ┃╭━━━━┳━╮╭━┳━━━┻╮ ╭╯
┃ ╭━━━╋ ╋━━━┃ ┣━━━┃ ┃ ╭╮ ┃┃ ╭━━━┫ ┃┃ ╭╮ ┃ ╭╮ ┫ ┃━━┫ ┃
┃ ┃   ┃ ┃ ┃━━━┫ ┃━━━┫ ╭╮ ┃┃ ┃   ┃ ╰┫ ╭╮ ┃ ┃┃ ┃ ┃━━┫ ╰╮
╰━╯   ╰━┻━━━━━┻━━━━━┻━╯╰━╯╰━╯   ╰━━┻━╯╰━┻━╯╰━┻━━━━┻━━╯		""")

menu()

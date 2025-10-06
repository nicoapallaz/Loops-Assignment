total = 0.00
order = 0
items = []
def price(x):
    if x == 1:
        return 2.75
    elif x == 2:
        return 3.25
    elif x == 3:
        return 6.50
    elif x == 4:
        return 2.00
    else:
        return "Not an option."

def item(x):
    if x == 1:
        items.append("Taco")
        return "You have selected a Taco"
    elif x == 2:
        items.append("Burrito")
        return "You have selected a Burrito"
    elif x == 3:
        items.append("Nachos")
        return "You have selected Nachos"
    elif x == 4:
        items.append("Soft Drink")
        return "You have selected a Soft Drink"




print("Welcome to Taco Palace! Please view the menu below and make a selection")
while order != 5:
    order = int(input(
        "Taco Palace Menu\n"
        "1. Taco\n"
        "2. Burrito\n"
        "3. Nachos\n"
        "4. Soft Drink\n"
        "5. Quit\n"
    ))
    if order == 5:
        break
    elif price(order) != "Not an option.":
        total += price(order)
        item(order)
    else:
        print("Not an option.")
print("Here is your order:")
for item in items:
    print(item)
print("Your total is: $" + str("{:.2f}".format(total)))
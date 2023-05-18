# I don't know if it should take that long,
# but at least it performs just like you wanted to.

from sys import exit    # Used for halting the program if it cannot find the file to read.

try: # Error catchers
    with open('menu.txt', 'r') as f:    # To read the file properly, file must be in the same path with the Python source code.
        lines = f.readlines()
        category_list = [line.split(";")[0] for line in lines[1:]]
        name_list = [line.split(";")[1] for line in lines[1:]]
        portion_list = [line.split(";")[2] for line in lines[1:]]
        price_list = [line.split(";")[3].strip('\n') for line in lines[1:]]

except FileNotFoundError:
    print("\nCannot find 'menu.txt'...")
    print("Restart the program after puting the file in the same path with the Python source code.\n")
    exit() # halts the program since there is no file.

# Opening the file to read the data and store it in row-order.

class Menu:
    def __init__(self, name, portionList, priceList):
        self.name = name
        self.portionList = portionList
        self.priceList = priceList

    def getName(self):
        return self.name

    def getPortion(self, indexNumber):
        return self.portionList[indexNumber]

    def getPrice(self, indexNumber):
        return self.priceList[indexNumber]

# Defining the Menu class to store the elements as an object.


patty_with_cheese = Menu(name_list[0], portion_list[0:3], price_list[0:3])
patty_with_beef = Menu(name_list[3], [portion_list[3]], [price_list[3]])
kids_cheeseburger = Menu(name_list[4], [portion_list[4]], [price_list[4]])
chicken_wrap = Menu(name_list[5], [portion_list[5]], [price_list[5]])

hummus_and_chicken_salad = Menu(name_list[6], portion_list[6:8], price_list[6:8])
classic_chicken_salad = Menu(name_list[8], portion_list[8:10], price_list[8:10])
chicken_caesar = Menu(name_list[10], portion_list[10:12], price_list[10:12])

chocolate_milkshake = Menu(name_list[12], portion_list[12:15], price_list[12:15])

fries = Menu(name_list[15], portion_list[15:18], price_list[15:18])

sauce = Menu(name_list[18], portion_list[18:20], price_list[18:20])

sour_cream_and_chive_baked_potato = Menu(name_list[20], [portion_list[20]], [price_list[20]])
chicken_and_cheddar_baked_potato = Menu(name_list[21], [portion_list[21]], [price_list[21]])

# Initializing the objects according to the file data.

cart = []   # This is the list to store the selected items.
var4 = 1    # Initializing the 'var4', a variable for menu navigation, before creating the while loop.

while var4 == 1:

    print("\nProduct Categories\n")

    print('1.', category_list[0], '\n'
          '2.', category_list[6], '\n'
          '3.', category_list[12], '\n'
          '4.', category_list[15], '\n'
          '5.', category_list[18], '\n'
          '6.', category_list[20])

    try:    # Error catchers.
        var1 = int(input("\nPlease select product category: "))
        if var1 not in range(1, 7):
            print("\nPlease enter a valid number!", '\n')
            continue
    except ValueError:
        print("\nPlease enter a numeric input!", '\n')
        continue

# Prints the first level of the menu, since it's just category, I didn't use objects for it.

    print('--------------------')

    if var1 == 1:
        print('\nProducts in', category_list[0], '\n')
        print('1.', patty_with_cheese.getName(), '\n'
              '2.', patty_with_beef.getName(), '\n'
              '3.', kids_cheeseburger.getName(), '\n'
              '4.', chicken_wrap.getName())

    elif var1 == 2:
        print('\nProducts in', category_list[6], '\n')
        print('1.', hummus_and_chicken_salad.getName(), '\n'
              '2.', classic_chicken_salad.getName(), '\n'
              '3.', chicken_caesar.getName())

    elif var1 == 3:
        print('\nProducts in', category_list[12], '\n')
        print('1.', chocolate_milkshake.getName())

    elif var1 == 4:
        print('\nProducts in', category_list[15], '\n')
        print('1.', fries.getName())

    elif var1 == 5:
        print('\nProducts in', category_list[18], '\n')
        print('1.', sauce.getName())

    elif var1 == 6:
        print('\nProducts in', category_list[20], '\n')
        print('1.', sour_cream_and_chive_baked_potato.getName(), '\n'
              '2.', chicken_and_cheddar_baked_potato.getName())

    try:    # Error catchers
        var2 = int(input("\nPlease select product name: "))
        if var2 not in range(1, 5):
            print("\nPlease enter a valid number!", '\n')
            continue
    except ValueError:
        print("\nPlease enter a numeric input!", '\n')
        continue

# Prints the second level of the menu by using the object's getName method.

    print('--------------------')

    if var1 == 1:
        if var2 == 1:
            print('\nPortions in', patty_with_cheese.getName(), '\n')
            print('1.', patty_with_cheese.getPortion(0), '\n'
                  '2.', patty_with_cheese.getPortion(1), '\n'
                  '3.', patty_with_cheese.getPortion(2))
        elif var2 == 2:
            print('\nPortions in', patty_with_beef.getName(), '\n')
            print('1.', patty_with_beef.getPortion(0))
        elif var2 == 3:
            print('\nPortions in', kids_cheeseburger.getName(), '\n')
            print('1.', kids_cheeseburger.getPortion(0))
        elif var2 == 4:
            print('\nPortions in', chicken_wrap.getName(), '\n')
            print('1.', chicken_wrap.getPortion(0))

    elif var1 == 2:
        if var2 == 1:
            print('\nPortions in', hummus_and_chicken_salad.getName(), '\n')
            print('1.', hummus_and_chicken_salad.getPortion(0), '\n'
                  '2.', hummus_and_chicken_salad.getPortion(1))
        elif var2 == 2:
            print('\nPortions in', classic_chicken_salad.getName(), '\n')
            print('1.', classic_chicken_salad.getPortion(0), '\n'
                  '2.', classic_chicken_salad.getPortion(1))
        elif var2 == 3:
            print('\nPortions in', chicken_caesar.getName(), '\n')
            print('1.', chicken_caesar.getPortion(0), '\n'
                  '2.', chicken_caesar.getPortion(1))

    elif var1 == 3:
        if var2 == 1:
            print('\nPortions in', chocolate_milkshake.getName(), '\n')
            print('1.', chocolate_milkshake.getPortion(0), '\n'
                  '2.', chocolate_milkshake.getPortion(1), '\n'
                  '3.', chocolate_milkshake.getPortion(2))

    elif var1 == 4:
        if var2 == 1:
            print('\nPortions in', fries.getName(), '\n')
            print('1.', fries.getPortion(0), '\n'
                  '2.', fries.getPortion(1), '\n'
                  '3.', fries.getPortion(2))

    elif var1 == 5:
        if var2 == 1:
            print('\nPortions in', sauce.getName(), '\n')
            print('1.', sauce.getPortion(0), '\n'
                  '2.', sauce.getPortion(1))

    elif var1 == 6:
        if var2 == 1:
            print('\nPortions in', sour_cream_and_chive_baked_potato.getName(), '\n')
            print('1.', sour_cream_and_chive_baked_potato.getPortion(0))
        elif var2 == 2:
            print('\nPortions in', chicken_and_cheddar_baked_potato.getName(), '\n')
            print('1.', chicken_and_cheddar_baked_potato.getPortion(0))

    try:    # Error catchers
        var3 = int(input("\nPlease select product portion: "))
        if var3 not in range(1, 5):
            print("\nPlease enter a valid number!", '\n')
            continue
    except ValueError:
        print("\nPlease enter a numeric input!", '\n')
        continue

# Prints the third level of the menu by using the object's getPortion method.

    print('--------------------')

    if var1 == 1:
        if var2 == 1:
            if var3 == 1:
                cart.append([patty_with_cheese.getName(), patty_with_cheese.getPortion(0), patty_with_cheese.getPrice(0)])
            elif var3 == 2:
                cart.append([patty_with_cheese.getName(), patty_with_cheese.getPortion(1), patty_with_cheese.getPrice(1)])
            elif var3 == 3:
                cart.append([patty_with_cheese.getName(), patty_with_cheese.getPortion(2), patty_with_cheese.getPrice(2)])

        elif var2 == 2:
            if var3 == 1:
                cart.append([patty_with_beef.getName(), patty_with_beef.getPortion(0), patty_with_beef.getPrice(0)])

        elif var2 == 3:
            if var3 == 1:
                cart.append([kids_cheeseburger.getName(), kids_cheeseburger.getPortion(0), kids_cheeseburger.getPrice(0)])

        elif var2 == 4:
            if var3 == 1:
                cart.append(([chicken_wrap.getName(), chicken_wrap.getPortion(0), chicken_wrap.getPrice(0)]))

    elif var1 == 2:
        if var2 == 1:
            if var3 == 1:
                cart.append([hummus_and_chicken_salad.getName(), hummus_and_chicken_salad.getPortion(0), hummus_and_chicken_salad.getPrice(0)])
            elif var3 == 2:
                cart.append([hummus_and_chicken_salad.getName(), hummus_and_chicken_salad.getPortion(1), hummus_and_chicken_salad.getPrice(1)])

        elif var2 == 2:
            if var3 == 1:
                cart.append([classic_chicken_salad.getName(), classic_chicken_salad.getPortion(0), classic_chicken_salad.getPrice(0)])
            elif var3 == 2:
                cart.append([classic_chicken_salad.getName(), classic_chicken_salad.getPortion(1), classic_chicken_salad.getPrice(1)])

        elif var2 == 3:
            if var3 == 1:
                cart.append([chicken_caesar.getName(), chicken_caesar.getPortion(0), chicken_caesar.getPrice(0)])
            elif var3 == 2:
                cart.append([chicken_caesar.getName(), chicken_caesar.getPortion(1), chicken_caesar.getPrice(1)])

    elif var1 == 3:
        if var2 == 1:
            if var3 == 1:
                cart.append([chocolate_milkshake.getName(), chocolate_milkshake.getPortion(0), chocolate_milkshake.getPrice(0)])
            elif var3 == 2:
                cart.append([chocolate_milkshake.getName(), chocolate_milkshake.getPortion(1), chocolate_milkshake.getPrice(1)])
            elif var3 == 3:
                cart.append([chocolate_milkshake.getName(), chocolate_milkshake.getPortion(2), chocolate_milkshake.getPrice(2)])

    elif var1 == 4:
        if var2 == 1:
            if var3 == 1:
                cart.append([fries.getName(), fries.getPortion(0), fries.getPrice(0)])
            elif var3 == 2:
                cart.append([fries.getName(), fries.getPortion(1), fries.getPrice(1)])
            elif var3 == 3:
                cart.append([fries.getName(), fries.getPortion(1), fries.getPrice(1)])

    elif var1 == 5:
        if var2 == 1:
            if var3 == 1:
                cart.append([sauce.getName(), sauce.getPortion(0), sauce.getPrice(0)])
            elif var3 == 2:
                cart.append([sauce.getName(), sauce.getPortion(1), sauce.getPrice(1)])

    elif var1 == 6:
        if var2 == 1:
            if var3 == 1:
                cart.append([sour_cream_and_chive_baked_potato.getName(), sour_cream_and_chive_baked_potato.getPortion(0), sour_cream_and_chive_baked_potato.getPrice(0)])
        elif var2 == 2:
            if var3 == 1:
                cart.append([chicken_and_cheddar_baked_potato.getName(), chicken_and_cheddar_baked_potato.getPortion(0), chicken_and_cheddar_baked_potato.getPrice(0)])

# This part determines which element is selected and stores their property in the cart list.

    print("\n1. Add New", '\n'  "2. Checkout")

    try:    # Error catchers
        var4 = int(input("\nPlease select an operation: "))
        while not(var4 == 1 or var4 == 2):
            print("\nInvalid input!", '\n')
            var4 = int(input("\nPlease select an operation: "))
    except ValueError:
        print("\nInvalid input causing ValueError! Restart the program.", '\n')
        exit()

    print('--------------------')

if var4 == 2:

    total = []
    for i in cart:
        total.append(float(i[2].strip(' $')))

# This part gets the total cost of the all selected items.

    print('\n')
col_width = max(len(word) for row in cart for word in row) + 2  # padding  
print('--'*col_width + "-------")

for row in cart:
    print("".join(word.ljust(col_width) for word in row))
print('--'*col_width + "-------")

print(" Total: ",'  '*(col_width-4),' ', '$', format(sum(total), '.2f'), sep='')

# This part prints the receipt with proper formating.

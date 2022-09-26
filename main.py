import numbers

#Header
print("                              ♡    ♡   ᕬ  ᕬ  ♡    ♡")
print("                              +   ♡  （⌯'-'⌯)   ♡   +               ʚ♡ɞ ")
print("                              ┏━━━━♡━━━━U━U━━━━♡━━━━┓")
print("         ʚ♡ɞ                  ♡ 𝒲𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝑜 𝒞𝒞𝒞 𝒞𝒶𝒻𝑒 ♡")
print("                              ┗━━━━♡━━━━━━━━━━━♡━━━━┛")
#Drinks Menu

# list of drinks
drink_list = ['Flat', 'White', 'Cappucino', 'Latte', 'Decaf', 'Hot Chocolate'] 

print("                        ╭───── ⋅ ⋅ ───── ✩ ────── ⋅ ⋅ ─────╮")
print("                        |          ૮⸝⸝> ̫ <⸝⸝ ა             |")    
print("                        |      $3.00     ..Flat White(1)   |")
print("                        |      $3.00      ..Cappucino(2)   |")
print("                        |      $3.50          ..Latte(3)   |")
print("                        |      $3.00          ..Decaf(4)   |")
print("                        |      $4.00  ..Hot Chocolate(5)   |")
print("                        ╰───── ⋅ ⋅ ───── ✩ ────── ⋅ ⋅ ─────╯")
print(":･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ")
#intro
name = input("Welcome to Cathedral Coffee Club\n\nWho shall we put the order name under?\n")
print("\nHello {}!".format(name))
quantity = input("How many coffees would you like today?\n")
is_coffee_number = False
try:
  quantity=int(quantity)  
  is_coffee_number = True
except:
  is_coffee_number=False
  
while is_coffee_number == False:
  quantity = input("Invalid! It has to be a number. How many coffees would you like today?\n")
  try:
    quantity=int(quantity)  
    is_coffee_number = True
  except:
    is_coffee_number=False


#if int(quantity) < 1: 
#    quantity = input("Invalid number, How many coffees would you like today?\n")

  
while int(quantity) < 1:
  quantity = input("Invalid number, How many coffees would you like today?\n")
  
#print("\nIs {} coffee(s) correct?" .format(quantity))
#answer = input("yes or no\n\n") 
#while str(answer) != "yes" and str(answer) != "no": 
 # answer = input("not supported answer, please type yes or no\n\n") 
order_counter = int(quantity)
coffee_counter = 0;
total_due = 0.00
receipt_content = ""

#orders = [order_counter]
#orders = [0 for i in range(order_counter)]
#orders = [[ [0] * 3 ] * order_counter ]
#orders = [3,order_counter]

orders = []
#[[0 for x in range(3)] for x in range(order_counter)]

order_line = ""
coffee_type =""
coffee_price=""
coffee_sugar=""

while (order_counter) > 0:
  coffee_counter = coffee_counter +1
  print("                              ♡    ♡   ᕬ  ᕬ  ♡    ♡")
  print("                              +   ♡  （⌯'-'⌯)   ♡   +                ʚ♡ɞ ")
  print("                              ┏━━━━♡━━━━U━U━━━━♡━━━━┓")
  print("         ʚ♡ɞ                  ♡ 𝒲𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝑜 𝒞𝒞𝒞 𝒞𝒶𝒻𝑒 ♡")
  print("                              ┗━━━━♡━━━━━━━━━━━♡━━━━┛")
  print("                        ╭───── ⋅ ⋅ ───── ✩ ────── ⋅ ⋅ ─────╮")
  print("                        |          ૮⸝⸝> ̫ <⸝⸝ ა             |")    
  print("                        |      $3.00     ..Flat White(1)   |")
  print("                        |      $3.00      ..Cappucino(2)   |")
  print("                        |      $3.50          ..Latte(3)   |")
  print("                        |      $3.00          ..Decaf(4)   |")
  print("                        |      $4.00  ..Hot Chocolate(5)   |")
  print("                        ╰───── ⋅ ⋅ ───── ✩ ────── ⋅ ⋅ ─────╯")
  coffee = input("please choose your coffee #{} using the numbers from 1-5\n\n".format(coffee_counter))
  
  while int(coffee) != 1 and int(coffee) != 2 and int(coffee) != 3 and   int(coffee) != 4 and int(coffee) != 5: 
    coffee = int(input("Please choose one number from 1-5\n\n"))
  
  if int(coffee) == 1:
    total_due = total_due +3
    #receipt_content = receipt_content + "\nFlat White  $3.00"
    #order_line = "\nFlat White  $3.00"
    #orders [1,0] = "Flat White"
    #orders [1,1] = "$3.00"
    coffee_type = "Flat White"
    coffee_price = "$3.00"
    
    
  elif int(coffee) == 2:
    total_due = total_due +3
    #receipt_content = receipt_content + "\nCappucino  $3.00"
    #order_line = "\nCappucino  $3.00"
    #orders [1,0] = "Cappucino"
    #orders [1,1] = "$3.00"
    coffee_type = "Cappuncino"
    coffee_price = "$3.00"
  elif int(coffee) == 3:
    total_due = total_due +3.5
    #receipt_content = receipt_content + "\nLatte  $3.50"
    #order_line = "\nLatte  $3.50"
    #orders [1,0] = "Latte"
    #orders [1,1] = "$3.50"
    coffee_type = "Latte"
    coffee_price = "$3.50"
  elif int(coffee) == 4:
    total_due = total_due +3
    #receipt_content = receipt_content + "\nDecaf  $3.00"
    #order_line = "\nDecaf  $3.00"
    #orders [1,0] = "Decaf"
    #orders [1,1] = "$3.00"
    coffee_type = "Decaf"
    coffee_price = "$3.00"
  elif int(coffee) == 5:
    total_due = total_due +4
    #receipt_content = receipt_content + "\nHot Chocolate  $4.00"
    #order_line = "\nHot Chocolate  $4.00"
    #orders [1,0] = "Hot Chocolate"
    #orders [1,1] = "$4.00"
    coffee_type = "Hot Chocolate"
    coffee_price = "$4.00"
  else:
    total_due = total_due

  sugar = input("Would you like sugar?\n yes or no?\n\n ")
  while sugar != "yes" and sugar != "no": 
    sugar = input("Would you like sugar?\n yes or no?\n ")
  if sugar == "yes":
    #receipt_content = receipt_content + " (with sugar)"
    #order_line = order_line + " (with sugar)"
    #orders[coffee_counter,2] = "(with sugar)"
    coffee_sugar = "(with sugar)"

  else:
    #receipt_content = receipt_content + " (without sugar)"
    #order_line = order_line + " (without sugar)"
    #orders[coffee_counter,2] = "(without sugar)"
    coffee_sugar = "(without sugar)"
    
 #orders[coffee_counter -1] = order_line
  orders.append([coffee_type, coffee_price, coffee_sugar])
  order_counter = order_counter -1
 # print("Your current total is ${}" .format(total_due))
#print("\n\n:･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･\nHere's your receipt\n {} " .format (receipt_content))
print("\n\n:･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･\nHere's your receipt\n ")
      
for x in orders:
  print(" {} {} {}".format (x[0], x[2], x[1]))
        

print("\nYour total amount to pay is ${:.2f} \n:･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･.☽˚｡･ﾟ✧:･.::･ﾟ✧:･" .format(total_due))


    
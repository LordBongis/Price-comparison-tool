#Class to sort the product information.
class Product:
  def __init__(self, name, cost, value):
    self.name = name
    self.cost = cost
    self.value = value
  #This function allows for the product information to be more easily printed/shown to the user
  def __str__(self):
    return "Product names: {}, Costs: ${}, Value {}/10 ".format(self.name, self.cost, self.value)
    
#List to hold the Product information
products = []
#This variable is the for the budget and by default is set to 0
budget = 0
#These two variables are to have constraints on what the products can cost, ie it cannot be 0, and the max price will depend on the budget they enter.
min_price = 1
max_price = 0

#This function lets the user choose how much their budget is.
def user_budget():
  global budget
  choosing_budget = True
  
  #While loop which allows for the user to input how much money is in their budget.
  while choosing_budget == True:
    budget_choice = input("Please enter the ammount of money you are willing to spend, this will act as your budget ").strip()
    if budget_choice.isnumeric():
      budget = int(budget_choice)
      
      choosing_budget = False
    else:
      print("The answer you enter must be a number! Please try again.")
      
#This function lets the user input product data, and allows for multiple products to be entered whist saving them to a list.
def product_information():
  making_products = True

  #While statment so that the product information inputs can be looped if needed.
  while making_products:
    name = input("Please enter a product's name ").strip().lower()
    cost = 0
    value = 0

    #While statment allows for the cost input to be looped upon failed input
    while cost == 0:
      cost_input = input("please enter the price of that product ")
      
      try:
        cost = int(cost_input)
        max_price = budget
        
        if cost >= max_price:
          #This is an error prevention if statment, so that if the cost of an item is larger then their budget, it cannot be entered.
          print("The product cannot cost more then your budget! Please enter a different product ")
          cost = 0
      except ValueError:
        print("The cost must be a valid number. Please try again. ")
        
#While loops allows for the value input to be looped on fail input
    while value == 0:
       value_input = input("Please enter the value of this product from 1 to 10. (1 being worst, 10 being best) ")
       try:
        value = int(value_input)
         
        if not 1 <= value <= 10:
          print("The value must be between 1 and 10. Please try again.")
          value = 0
          
       except ValueError:
         print("The value must be a valid number. Please try again.")
      
    else:
      product_data = Product(name, cost, value)
      products.append(product_data)
      print("Information stored! ")
      #This allows for the product list to be printed will all of the products in the list.
      print("Current product list: ")
      for product in products:
        print(product)
      additional_product = input("Would you like to enter another product and its information? Y/N ").strip().lower()
      #This if statment loops the product creation on a yes input, or proceds to Analysation on no.
      if additional_product == "yes" or additional_product == "y":
        print("Next product! ")
        
      elif additional_product == "no" or additional_product == "n":
        making_products = False
        print("Moving on to analysation! ")
        
      else:
        print("The answer you enter must be either yes or no! Please try again. ")
        
    

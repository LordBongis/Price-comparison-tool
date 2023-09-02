#Class to sort the product information.
class Product:
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost
  #This function allows for the product information to be more easily printed/shown to the user
  def __str__(self):
    return "Product names: {}, Costs: ${}".format(self.name, self.cost)
    
#List to hold the Product information
products = []
#This variable is the for the budget and by default is set to 0
budget = 0
#These two variables are to have constraints on what the products can cost, ie it cannot be 0, and the max price will depend on the budget they enter.
min_price = 1
max_price = 0
def user_budget():
  global budget
  choosing_budget = True
  
  #While loop which allows for the following question to be able to loop when a wrong input is entered.
  while choosing_budget == True:
    budget_choice = input("Please enter the ammount of money you are willing to spend, this will act as your budget ").strip()
    if budget_choice.isnumeric():
      budget = int(budget_choice)
      
      choosing_budget = False
    else:
      print("The answer you enter must be a number! Please try again.")
      

def product_information():
  making_products = True
  
  while making_products == True:
    name = input("Please enter a product's name ").strip().lower()
    cost = int(input("Please enter the price of that product "))
    max_price = budget
    
    if cost >= max_price:
      print("The product cannot cost more then your budget! Please enter a different product")
      
    else:
      product_data = Product(name, cost)
      products.append(product_data)
      print("Information stored! ")
      print("Current product list: ")
      for product in products:
        print(product)
      additional_product = input("Would you like to enter another product and its information? Y/N ").strip().lower()
      
      if additional_product == "yes" or additional_product == "y":
        print("Next product! ")
        
      elif additional_product == "no" or additional_product == "n":
        making_products = False
        print("Moving on to analysation! ")
        
      else:
        print("The answer you enter must be either yes or no! Please try again. ")
        
    

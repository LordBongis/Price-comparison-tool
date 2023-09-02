#Class to sort the product information.
class Product:
  def product_initialiser(self, name, cost):
    self.name = name
    self.cost = cost
    
#List to hold the Product information
products = []
#This variable is the for the budget and by default is set to 0
budget = 0
def user_budget():
  global budget
  choosing_budget = True
  
  #While loop which allows for the following question to be able to loop when a wrong input is entered.
  while choosing_budget == True:
    budget_choice = (input("Please enter the ammount of money you are willing to spend, this will act as your budget ")).strip()
    if budget_choice.isnumeric():
      budget = int(budget_choice)
      choosing_budget = False
    else:
      print("The answer you enter must be a number! Please try again.")
      



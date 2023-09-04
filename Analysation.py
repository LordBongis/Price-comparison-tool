#Importing data is a nesesity to get the product info and budget info.
import Data

def calculate_product_value(products, budget):
  #These variables are required in the calculation to get the best product and its ratio.
  best_value_product = None
  best_value_ratio = 0 
  #For loop so that it can analyse all the products.
  for product in products:
    if product.cost <= budget:
      value_ratio = calculate_value(product) / product.cost
      #If statment to check the value ratio against the current best ratio and then change it if required.
      if value_ratio > best_value_ratio:
        best_value_ratio = value_ratio
        best_value_product = product
  #If statment to inform the user on the best product.
  if best_value_product:
    print("The best value for money is {} with a price to value ratio of {}".format(best_value_product.name, best_value_ratio))
  else: 
    print("No products fit within the budget. ")
#This function simply returns the product value.
def calculate_value(product):
  return product.value
  
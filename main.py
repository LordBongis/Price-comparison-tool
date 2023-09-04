#This simply imports the other files so that they can be run through the main.py file.
import Intro
import Data
import Analysation

#This runs the files in the order the program requires ie Intro -> Data -> Analyze -> End
looping_program = True
while looping_program == True:
  Intro.Instructions()
  Data.user_budget()
  Data.product_information()
  Analysation.calculate_product_value(Data.products, Data.budget)
  
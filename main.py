#This simply imports the other files so that they can be run through the main.py file.
import Intro
import Data
import Analysation
import EndCap

#This runs the files in the order the program requires ie Intro -> Data -> Analyze -> End
looping_program = True
Intro.Instructions()
Data.user_budget()

#While allows for the program to loop the products and get a new calculation.
while looping_program == True:
  Data.product_information()
  Analysation.calculate_product_value(Data.products, Data.budget)
  looping_program = EndCap.stop_looping_program(looping_program)
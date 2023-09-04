

#This function allows the user to loop the product creation and analysaton.
def stop_looping_program(looping_program):
  asking_loop = True
  #while loop for error prevention
  while asking_loop == True:
    loop_ask = input("Would you like to add more products to the list and run the calculation again? ").strip().lower()

    #If statment so that the different answers to the loop_ask input can be used differently.
    if loop_ask == "yes" or loop_ask == "y":
      print("Looping program! ")
      asking_loop = False
    
    elif loop_ask == "no" or loop_ask == "n":
      asking_loop = False
      looping_program = False

    else:
      print("You must enter Yes or no. Please try again")
    #returning the looping_program so the main file can decide weither or not to loop the program.
    return looping_program
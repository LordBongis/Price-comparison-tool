#This function gives the users the oppertunity to recive instructions on the program's use.
def Instructions():
  giving_instructions = True
  while giving_instructions == True:
    requires_instruction = input("Would you like instructions? Or have you used this program before? Y/N ").strip().lower()
    #Simple if statment to check what the user answered the input with and giving appropreate responses.
    if requires_instruction == "yes" or requires_instruction == "y":
      print("This program is made to help you calculate which out of a set of products are best to purchase baised on a budget you will set. The program is going to ask for your budget which is how much you are willing to spend, and then you will fill in the information of products untill you have a list you are satisfied with. From there the program will analyze them and give its recomendation to you.")
      giving_instructions = False

    elif requires_instruction == "no" or requires_instruction == "n":
      giving_instructions = False

    else:
      print("Please enter either Yes, or No to this question")

  return
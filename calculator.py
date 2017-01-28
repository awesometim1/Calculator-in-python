import random
#GLOBAL VARIABLE!!! CHOICE
choice = 0
#Methods for the calculations

#Addition
def add(x , y):
  sum2 = x + y
  return sum2
#Subtraction
def sub(x , y):
  diff2 = x - y
  return diff2
#Multiplication
def mult(x , y):
  prod2 = x * y
  return prod2
#Division
def div(x , y):
  quot2 = x / y
  return quot2
def choices():
 #Addition Choice
 if choice == 1:
   print("\n \n \nPlease Enter two numbers that you would like to add")
   sum1 = add(int(input()) , int(input ()))
   print("" , sum1, "\n")
   main()
 #Subtraction Choice
 elif choice == 2:
   print("\n \n \nPlease Enter two numbers that you would like to subtract")
   diff1 = sub(int(input(":")), int(input (":")))
   print("" , diff1 , "\n")
   main()
 #Multiplication Choice 
 elif choice == 3:
   print("\n \n \nPlease Enter two numbers that you would like to multiply")
   prod1 = mult(int(input(":")), int(input (":")))
   print("" , prod1, "\n")
   main()
 #Division Choice 
 elif choice == 4:
   print("\n \n \nPlease Enter two numbers that you would like to divide")
   quot1 = div(int(input(":")), int(input (":")))
   print("" , quot1, "\n")
   main()
#Random Number Generator  
 elif choice == 5:
   print("\n \n \nPlease Enter a range from minimum to maximum")
   rand = random.randint(int(input(":")), int(input (":")))
   print("Generating...")
   print(rand , "is your random number!" , "\n")
   main()
#Exception Handler
 else:
   print("ERROR")
   quit()
   
#Main Menu
def main():
  print("Welcome to the multifunction calculator. Please select an option to get started.")
  print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Random number generator with range")
  global choice
  choice = int(input(":"))
  choices()
  
#First time starter
main()

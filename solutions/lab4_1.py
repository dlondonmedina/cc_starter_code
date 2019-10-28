def is_even():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))
   out = None

   if user_data % 2 == 0:
      out = True 
   else: 
      out = False

   return out 

def multi_condition():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))

   if user_data == 0:
      print("Don't be such a zero!")
   elif user_data < 0:
      print("Negative Nelly!")
   elif user_data % 2 == 0:
      print("Even Steven!")
   else:
      print("Positively odd!")

   return None


def is_underage():

   age = int(input("How old are you? "))

   if age >= 21:
      print("You may drink, smoke, and drive if you wish!")
   elif age >= 18:
      print("You may smoke and drive!")
   elif age >= 16:
      print("You may drive!")
   else:
      print("Enjoy your bike, kid!")

   # So the tests fail and they don't throw errors
   return None

def countdown():

   for i in range(10, -1, -1):
      print(i)

   # So the tests fail and they don't throw errors
   return None

def guessing_game(num):
   # This is a guessing game. I have set up a parameter that will be
   # a random integer that your user will have to try to guess.
   # To use num in your condition, you should write something like
   # 
   # if user_input == num: 
   #    
   # You should give your user at most 10 guesses to guess
   # the number. If the guess is too high or too low, you should tell 
   # them "Too High!" or "Too Low!" with the print statement.
   # If they guess the number, you should tell them "You win!"
   # otherwise, if they run out of guesses, tell them, "You lose!"
   # If they want to, your condition should also check for "q" and 
   # if the user enters that the program should exit, saying 
   # "Goodbye, quitter!"
   # No, it's not a very nice program. 
   count = 0
   while count < 10:
      user_input = input("Guess a number! ")
      if user_input == "q":
         print("Goodbye, quitter!")
         return None 
      user_input = int(user_input)
      if user_input > num:
         print("Too High!")
      elif user_input < num:
         print("Too Low!")
      else:
         print("You win!")
         return None 
      count += 1

   print("You Lose!")   
   # So the tests fail and they don't throw errors
   return None
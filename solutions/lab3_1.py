def sums():
   
   first_sum = 2 + 2
   first_sum = first_sum * 10
   secret = first_sum + 2

   return secret

def string_manip(first_name):

   name = first_name
   all_caps = name.upper()
   all_lowercase = name.lower()
   first_five_letters = name[:5]
   last_two_letters = name[-2:]

   return [all_caps, all_lowercase, first_five_letters, last_two_letters]

def greeter_bot():

   fname = input("Hi, I'm Greeter bot! what is your name? ")
   print("Hello, {}!".format(fname))

def temp_calculator():

   # TODO: Write code that prompts the user for a temperature in degrees
   # fahrenheit and prints the equivalent temperature in degrees celsius.
   # The formula is C = (F - 32) * (5/9). 
   f = float(input("What temperature is it? "))
   c = (f - 32) * (5/9)
   print(c)

def equitable_bill_splitter():
   
   # Get a count of people from the user and store value
   people = int(input("How many people are paying? "))
   # Initialize array for salaries
   salaries = []
   # Initialize a total salaries variable
   total = 0
   
   # Iterate through the number of people and add their salary to the
   # total and to a new index in the salaries list.
   for i in range(people):
      sal = int(input("What is the salary of person {}?".format(i+1)))
      total += sal
      salaries.append(sal)
   
   # Prompt user for total bill. This should be float?
   total_bill = int(input("How much is the bill? "))
   
   # Loop through salaries, printing out the amount the person should pay
   # based on their percentage of the salary total.
   for j in range(len(salaries)):
      print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j]/total)), 2)))

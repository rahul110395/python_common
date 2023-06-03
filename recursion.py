def check_odd_even(my_num):
   if (my_num < 2):
      return (my_num % 2 == 0)
   return (check_odd_even(my_num - 2))
my_number = int(input("Enter the number that needs to be checked:"))
if(check_odd_even(my_number)==True):
   print("The number is even")
else:
   print("The number is odd!")
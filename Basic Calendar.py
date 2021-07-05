# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
  

# To take month and year input from the user
# year    yy = 2014  
# month   mm = 11  

# display the calendar
print(calendar.month(yy, mm))

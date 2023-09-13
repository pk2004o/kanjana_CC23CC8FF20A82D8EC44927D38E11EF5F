Year=int(input("Enter Year to be checked: "))
if(Year%4==0 and Year%100!=0 or Year%400==0):
  print("The Year is a leap year!")
else:
  print("The Year isn't a leap year!")
def leap(year):
    if(year % 4 ==0 and year % 100 != 0) or (year%400 == 0):
           return True
    else:
        return False
year = int(input(""))
if leap(year):
    print(year, "- leap year")
else:
   print(year, "- not a leap year")

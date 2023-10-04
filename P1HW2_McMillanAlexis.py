# This program calculates and displays the travel expenses and remaining balance

# 10/03/2023
 
# CTI-110 P1HW2 - Travel Expense

# Alexis McMillan

print("This program calculates and displays travel expenses")
print("Enter Budget:",end =" ")
budget=int(input())
print("Enter your travel destination:",end =" ")
place =input()
print("How much do you think you will spend on gas?",end=" ")
gas=int(input())
print("Approximately, how much will you need for accomodation/hotel?",end =" ")
hotel=int(input())
print("Last, how much do you need for food?",end=" ")
food=int(input())
print("-----------Travel Expenses------------")
print("Location: "+place)
print("Initial Budget: "+str(budget))
print()
print("Fuel: "+str(gas))
print("Accomodation: "+str(hotel))
print("Food: "+str(food))
print()
print("Remaining Balance"+str(budget-gas-hotel-food))


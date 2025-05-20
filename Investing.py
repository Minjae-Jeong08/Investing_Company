import random
import sys
from Company import Company

#yes
#x= random.randrange(0,100)

#print(x)

#def Makecompany():

print("Welcome to a Virtual Investing Game!")
print("You have 100 dollars of sid money to start your investing.")
print("Every turn you invest something, the values of the stock will going to change")
print("Please enjoy playing!")

new_company = Company("Tech Innovators", 500000)
new_company.display_info()


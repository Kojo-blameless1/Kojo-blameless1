#This programe calculates the total sales in a week
'''list = []

for days in range(1,8):
    sales = int(input(f'Enter sales of day_{days} '))
    list.append(sales)

results = sum(list)
print(f'SUM: {results:,.2f}')'''
import random

#lotery
lotery_numbers = []
for i in range(1,8):
    number = random.randint(0,9)
    lotery_numbers.append(number)
print(lotery_numbers)
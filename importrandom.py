import random
#create n empty list
lottery_numbers = list()

# loops
for num in range(7):
    numbers = random.randint(1,7) 
    lottery_numbers.append(numbers)
for i in lottery_numbers:
    print(i, end=' ' )

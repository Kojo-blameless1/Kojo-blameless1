
sales = float(input("Enter sales for the month: "))

day_off = 1.25 * 90000
bonus = 500

if sales >= 100000 and sales < int(day_off):
    print(f"congratulations you have a bonus of ${bonus} " )

elif sales >= day_off:
    print(f"congratulations You have a Day off and a bonus of $ {bonus} ")

else:
    print(f"Employees will not get a day off and no bonus  this month.")




 
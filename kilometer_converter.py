def convert(num):
    CONST = 0.6214
    miles = num * CONST
    return miles

kilometer = float(input('enter:'))
miles = convert(kilometer)
print(f'The Distance is {miles:,.2f} miles')
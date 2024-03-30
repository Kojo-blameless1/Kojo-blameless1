def max(num_1,num_2):
    if num_1 < num_2:
        return num_2
    else:
        return num_1


number_1 = int(input('enter:'))
number_2 = int(input('enter:'))
max_value = max(number_1,number_2)
print('The maximum value is : ',max_value)



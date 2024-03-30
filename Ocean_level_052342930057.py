# This programe calculates the ocean level for 25 years
# rising rate per anum
RISING_RATE = 1.6
print("YEARS\t\t OCEAN_LEVEL")
print("_________________________")
#calculating the ocean level the for loop
for years in range(1,26):
    ocean_level = years * RISING_RATE
    #Displaying the ocean level for every year
    print(f'{years} \t\t\t {ocean_level:.2f}')



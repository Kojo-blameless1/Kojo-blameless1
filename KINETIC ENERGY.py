# This program calculates Kinetic Energy
def kinetic_energy(mass,velocity):
    CONST = 0.5
    kinetic = CONST * (mass * velocity ** 2)
    return kinetic
#Take input for mass and Velocity
mass = float(input("Enter mass in kilos: "))
velocity = float(input("Enter velocity in meter per second: "))
#Display the Kinetic Energy
print(f'Kinetic Energy: {kinetic_energy(mass,velocity):,.2f}')


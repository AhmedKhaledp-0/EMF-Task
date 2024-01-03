import numpy as np
import math
def ConvertPointFromCartesianToCylindrical():
    cartesian_x = float(input("Enter Cartesian (X) value: "))
    cartesian_y = float(input("Enter Cartesian (Y) value: "))
    cartesian_z = float(input("Enter Cartesian (Z) value: "))
    #Calculate cylindrical RHO & PHI
    Cylindrical_rho = math.sqrt(cartesian_x**2+cartesian_y**2)
    Cylindrical_phi = math.degrees(math.atan(cartesian_y / cartesian_x))
    #Print Cylindrical RHO & PHI & Z
    print('\u03C1 = {0:.2f}'.format(Cylindrical_rho))
    print('\u03C6 = {0:.2f}'.format(Cylindrical_phi))
    print('z = {0:.2f}'.format(cartesian_z))
def main():
    ConvertPointFromCartesianToCylindrical()

if __name__ == "__main__":
    main()


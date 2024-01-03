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

def ConvertPointFromCylindricalToCartesian():
    Cylindrical_rho = float(input("Enter \u03C1 value: "))
    Cylindrical_phi = float(input("Enter \u03C6 value: "))
    Cylindrical_Z = float(input("Enter z value: "))
    cartesian_x = (Cylindrical_rho * math.cos(math.radians(Cylindrical_phi)))
    cartesian_y = (Cylindrical_rho * math.sin(math.radians(Cylindrical_phi)))
    cartesian_z = Cylindrical_Z
    print('x = {0:.2f}'.format(cartesian_x))
    print('y = {0:.2f}'.format(cartesian_y))
    print('z = {0:.2f}'.format(cartesian_z))

def main():
    #ConvertPointFromCartesianToCylindrical()
    ConvertPointFromCylindricalToCartesian()
if __name__ == "__main__":
    main()


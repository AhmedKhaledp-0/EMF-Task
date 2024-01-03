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

def ConvertVectorFromCartesianToCylindrical():
    cartesian_Ax = float(input("Enter Cartesian (Ax) value: "))
    cartesian_Ay = float(input("Enter Cartesian (Ay) value: "))
    cartesian_Az = float(input("Enter Cartesian (Az) value: "))
    phiRad = math.atan(cartesian_Ay / cartesian_Ax)
    convertingMatrix = np.matrix([[math.cos(phiRad), math.sin(phiRad), 0], [-math.sin(phiRad),math.cos(phiRad),0],[0, 0,1]])
    cartesianMatrix = np.matrix([[cartesian_Ax], [cartesian_Ay], [cartesian_Az]])
    vectorOnCylindrical = np.matmul(convertingMatrix, cartesianMatrix)
    print('A\u03C1 = {0:.2f}'.format(vectorOnCylindrical.item(0)))
    print('A\u03C6 = {0:.2f}'.format(vectorOnCylindrical.item(1)))
    print('Az = {0:.2f}'.format(vectorOnCylindrical.item(2)))

def ConvertVectorFromCylindricalToCartesian():
    cylindrical_Ap = float(input("Enter Cylindrical (A\u03C1) value: "))
    cylindrical_Ao = float(input("Enter Cylindrical (A\u03C6) value: "))
    clyindrical_Az = float(input("Enter Cylindrical (Az) value: "))
    phiRad = math.atan(cylindrical_Ao / cylindrical_Ap)
    convertingMatrix = np.matrix([[math.cos(phiRad), -math.sin(phiRad), 0], [math.sin(phiRad),math.cos(phiRad),0],[0, 0,1]])
    CylindricalMatrix = np.matrix([[cylindrical_Ap], [cylindrical_Ao], [clyindrical_Az]])
    vectorOnCartesian = np.matmul(convertingMatrix, CylindricalMatrix)
    print('Ax = {0:.2f}'.format(vectorOnCartesian.item(0)))
    print('Ay = {0:.2f}'.format(vectorOnCartesian.item(1)))
    print('Az = {0:.2f}'.format(vectorOnCartesian.item(2)))
    
def promptForNewValues():
    user_input = input("\nDo you want to enter new values? (yes/no): ").lower()
    if user_input != 'yes':
        return False
    else:
        main()
        return True

def main():
    while True:
        x = int(input("What do you want to Convert \nPoint\n 1.Cartesian to Cylindrical \n 2.Cylindrical to Cartesian\nVectors\n 3.Cartesian to Cylindrical\n 4.Cylindrical to Cartesian\n"))
        if (x == 1):
            ConvertPointFromCartesianToCylindrical()
            if not promptForNewValues():
                break
        elif (x == 2):
            ConvertPointFromCylindricalToCartesian()
            if not promptForNewValues():
                break
        elif (x == 3):
            ConvertVectorFromCartesianToCylindrical()
            if not promptForNewValues():
                break
        elif (x == 4):
            ConvertVectorFromCylindricalToCartesian()
            if not promptForNewValues():
                break
        else:
            print("you enterd a wrong vlaue")
        if not promptForNewValues():
            break
if __name__ == "__main__":
    main()


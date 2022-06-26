from math import pi

R = float(input("Enter the radius: "))

D = (2 * R)
C = (2 * pi  * R)
A = (4 * pi * R * R)
V = (4 / 3 * pi * R * R * R)

print("The Diameter is: " + str(D))
print("The Circumference is: " + str(C))
print("The Surface Area is: " + str(A))
print("The Volume is: " + str(V))

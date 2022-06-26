height = float(input("Enter the height from which the ball is dropped: "))

bounceIndex = float(input("Enter the bounciness index of the ball: "))

bounceNumber = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

distance = height

for i in range(bounceNumber-1):
    height *= bounceIndex
    distance += 2 * height


distance += height * bounceIndex
print("\nTotal distance traveled is: " + str(distance) + " feet.")

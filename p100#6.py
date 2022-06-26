iterationsCount = int(input("Specify number of iterations: "))

total = 0

for i in range(iterationsCount):
    total += ((-1) ** i) * (1 / ((2 * i) + 1))

total *= 4

print("Calculated value of pi with specified number of iterations is: " + str(total))

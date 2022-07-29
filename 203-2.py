import math

t=0.00001
approx=1.0
num = float(input("Enter a positive number or press Enter to quit: "))

def newton(number,approx):
    approx=(approx+number/approx)/2
    diffvalue =abs(number-approx**2)

    if diffvalue<= t:
        return approx
    else:
        return newton(number,approx)
    
print("Program's estimate: ", newton(num, approx))
print("Python's estimate: ", math.sqrt(num))

sal = float(input("Enter your starting salary: "))
percent = float(input("Enter the increase percentage: "))
years = int(input("Enter the number of years: "))

print("\nYear Salary")

for i in range(years):
    print(i+1, sal)
    sal = round(sal + (sal * percent)/100, 2)


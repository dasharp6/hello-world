hourlyWage = float(input("Enter hourly wage: "))
regularHours = float(input("Enter total regular hours: "))
overTimeHours = float(input("Enter total Overtime hours: "))

overTimePay = overTimeHours * (1.5 * hourlyWage)
weeklyPay = round(hourlyWage * regularHours + overTimePay, 2)

print(weeklyPay)

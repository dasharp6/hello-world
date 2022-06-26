def main():


    f_name = input("Enter the name of the file: ")


    f_obj = open(f_name)


    print()


    print("%-10s%10s%15s" %("Name","Hours","Total Pay"))

    for curr_line in f_obj:

        values = curr_line.split()

        name = values[0]

        wage = float(values[1])

        hours = int(values[2])
        
        total_pay = wage*hours

        print("%-10s%10s%15.2f" %(name,hours,total_pay))

    f_obj.close()

main()

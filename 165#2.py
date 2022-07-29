fileName = input("Please enter the file name: ")
o = open(fileName, 'r')
l = o.readlines()    
while(1):       
    print("There are", len(l), "lines in file.")
    n = int(input("Please enter the line number you want: "))
    if(n == 0):
        break
    else:
        print(l[n-1])

sourceFile = input("Enter the input file name: ")
destinationFile = input("Enter the output file name: ")

try:
    f = open(sourceFile)
    out = open(destinationFile, "w")
    for line in f:
        out.write(line)
    f.close()
    out.close()
    
except FileNotFoundError as fnfe:
    
    print(sourceFile,"not found")

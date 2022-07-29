def printALL(seq):
    if seq:
        print("sequence:",seq)
        print(seq[0])
        printALL(seq[1:])
printALL("Hey there!")
printALL((8,6,7,5,3,0,9))
printALL([8,6,7,5,3,0,9])

def getAvg(l):
    total = 0
    for number in l:
        total += float(number)
    return total/len(l)

def main():
    fname = input("Enter a file name:")

    try:
        numbers = open(fname, "r").read().split()
        avg = getAvg(numbers)
        print("Average is", avg)
    except:
        print("Not working")
main()        

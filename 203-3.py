def newtonSquare(x, estimate=1.0):
    if abs(x-estimate ** 2) <= 0.000001:
        return estimate
    else:
        return newtonSquare(x, (estimate + x / estimate) / 2)

def main():
    while(True):
        num = input("Enter a positive number or press Enter to quit: ")
        if num.strip() == ''  or num == '/return':
             break

        print()
        print('%-35s%s' % ("Program's estimate: ", str(newtonSquare(int(num)))))
        print('%-35s%s\n' % ("Python's estimate: ", str(int(num)**0.5)))


main()

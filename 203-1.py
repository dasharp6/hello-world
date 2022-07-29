def newton(n):

        t = 0.000001
        esti = 1.0

        while True:

                esti = (esti + n / esti) / 2
                dif = abs(n - esti ** 2)
                if dif <= t:

                        break

        return esti

def main():

        while True:

                try:
                        n = int(input("Enter a number (Press Enter to quit):"))

                        print("newton = %0.15f" % newton(n))

                except:

                        return

main()

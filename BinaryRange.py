# Global variables
Scheme = ""
Bits = 0

def main():
    while True:
        # Main terminal
        print("-------------------------")
        Scheme = input("Scheme: ").upper()

        # Command dispatcher
        if Scheme == "B":
            base_2()
        elif Scheme == "SB":
            signed_bit()
        elif Scheme == "TC":
            twos_complement()

def base_2():
    # Input/Output
    display()
    print(str(Bits) + "bB on [0, " + str(2**Bits - 1) + "]")

def signed_bit():
    # Input/Output
    display()
    print(str(Bits) + "bSB on [" + str(-(2**(Bits - 1) - 1)) + ", " + str(2**(Bits - 1) - 1) + "]")

def twos_complement():
    # Input/Output
    display()
    print(str(Bits) + "bTC on [" + str(-2**(Bits - 1)) + ", " + str(2**(Bits - 1) - 1) + "]")

def display():
    # Enter bit number
    global Bits
    Bits = bit_number()

    # Output/calculate interval
    print("")

def bit_number():
    while True:
        # Local variable input
        print("")
        Bits = input("Bits: ")

        if Bits.isdigit() and int(Bits) >= 1 and int(Bits) == float(Bits):
            return int(Bits)
        else:
            print("")
            print("Error!")

# Run the program
main()

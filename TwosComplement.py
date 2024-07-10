# Global variables
Input = ""
Denary = 0
Binary = ""

def main():
    global Denary, Binary
    
    while True:
        # Reset variables
        Denary = 0
        Binary = ""

        # Main terminal
        print("--------------------------------------------------")
        Input = input("(1)D>B (2)B>D: ")

        # Command dispatcher
        if Input == "1":
            print("")
            Denary = int(input("Denary value: "))
            tc_denary_binary(Denary)

        elif Input == "2":
            print("")
            Binary = input("TC value: ")
            tc_binary_denary(Binary)

def tc_denary_binary(den_val):
    global Binary
    
    # Convert to binary
    Binary = binary_conversion(abs(den_val))

    # Sign check
    if den_val == abs(den_val):
        # Output
        print("")
        print(str(den_val) + " = " + Binary)

    else:
        # Convert to two's complement
        Binary = trim_end(Binary)

        # Reduce excess leading 1
        if Binary[0] == "1" and Binary[1] == "1":
            Binary = Binary[1:]

        # Output
        print("")
        print(str(den_val) + " = " + Binary)

def tc_binary_denary(bin_val):
    # Local variables
    temp_bin_val = bin_val

    # Handle negative numbers
    if bin_val[0] == '1':
        bin_val = complement_bits(bin_val)
        den_val = -int(bin_val, 2) - 1
    else:
        den_val = int(bin_val, 2)

    # Output
    print("")
    print(temp_bin_val + " = " + str(den_val))

def binary_conversion(num):
    # Local variables
    remainder = 0
    bits = ""

    # Convert to binary
    if num == 0:
        bits = "0"
    else:
        while num > 0:
            remainder = num % 2
            bits = str(remainder) + bits
            num = num // 2

    return "0" + bits

def trim_end(bin_val):
    # Local variables
    position = 0
    bit = ""
    index = 0

    # Find final 1
    while bin_val[position] != "1":
        position = len(bin_val) - 1 - index
        bit = bin_val[position]
        index += 1

    trim2 = bin_val[position:]
    print(trim2)

    # Complement preceding bits
    trim1 = complement_bits(bin_val[:position])

    return trim1 + trim2

def complement_bits(bin_val):
    # Local variables
    cbinary = ""

    # Complement bits
    for bit in bin_val:
        if bit == "0":
            cbinary += "1"
        else:
            cbinary += "0"

    return cbinary

# Call the main function to start the program
main()

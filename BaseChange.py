while True:
    
     # Local variables
    num1 = 0
    base1 = 0
    num2 = ""
    base2 = 0
    temp_num = 0
    num_base1 = 0
    remainder = 0

    # Inputs
    num1 = str(input("Num1:"))
    base1 = int(input("Base1:"))
    base2 = int(input("Base2:"))

    # Base validation
    while (base1 < 2 or base1 > 36) or (base2 < 2 or base2 > 36):
        if base1 < 2 or base1 > 36:
            print("Error! Base1 on [2, 36]")
            base1 = int(input())
        else:
            print("Error! Base2 on [2, 36]")
            base2 = int(input())

    num_base1 = num1

    # Ensure base 10
    if base1 != 10:
        for digit in range(len(str(num1))):
            try:
                temp_num += int(str(num1)[digit]) * base1 ** (len(str(num1)) - 1 - digit)
            except ValueError:
                temp_num += (ord(str(num1)[digit]) - 87) * base1 ** (len(str(num1)) - 1 - digit)

        num1 = temp_num

    # Convert base
    while num1 != 0:
        remainder = int(num1) % base2

        if remainder >= 10:
            num2 = chr(remainder + 87) + num2
        else:
            num2 = str(remainder) + num2

        num1 = int(num1) // base2

    # Output
    print("")
    print("{}_{} = {}_{}".format(num_base1, base1, num2, base2))
    print("----------------------------------------")
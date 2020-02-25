def factor():
    """ Outputs the prime factorisation of an integer input greater than one
    """
    number = input("Input a integer > 1: ")
    if number.isdigit() == False or int(number) <= 1:
        print(f"{number} is not an integer > 1")
    else:
        number = int(number)
        i = 2
        while number != 1:
            if number % i == 0:
                print (i)
                number = number / i
            else: 
                i += 1
 
factor()
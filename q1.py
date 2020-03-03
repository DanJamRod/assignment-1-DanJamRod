def factor():
    """ Outputs the prime factorisation of an integer input greater than one
    """
    number = input("Input a integer > 1: ")
    if number.isdigit() == False or int(number) <= 1: # Can't prime factorise a negative number, a non-integer, 0, or 1
        print(f"{number} is not an integer > 1")
    else:
        number = int(number)
        i = 2 # First possible prime factor
        while number != 1: # Stops function when no remainder left
            if number % i == 0: # Checks whether number is divisable by the current possible prime factor
                print (i) # If it is divisible, then prints as is prime factor
                number = number / i # If it is divisible, divide the number by the prime factor and check whether it divides again
            else: 
                i += 1 # If not a prime factor, checks next number
 
factor()
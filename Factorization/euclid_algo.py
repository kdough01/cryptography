def euclid_algo(a,b):

    """
    This is a function for Euclid's Algorithm, the most efficient way
    of finding the greatest common divisor of two integers.

    Parameters:
    a : int - any integer
    b: int - any integer
    """

    # If this if statement does not hold true we simply re-run the program swapping the parameters.
    if a>b:

        r=a%b
        r_list = []
        b_list = []

        if r == 0:
            r_list.append(r)
            b_list.append(b)

        else:
            while r != 0 and b != 0:

                x = int(round(a / b, 0))
                r = a % b

                r_list.append(r)
                b_list.append(b)

                a, b = b, r

        # You can optionally print out the quotients and remainders from the iterations.
        #print(b_list)
        #print(r_list)

        return b_list[-1]

    else:
        return euclid_algo(b, a)
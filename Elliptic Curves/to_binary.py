import math as m

def to_binary(n):

    binary = []
    while n>=1:

        binary.append(n%2)
        n = m.floor(n/2)

    binary = binary[::-1]

    return binary
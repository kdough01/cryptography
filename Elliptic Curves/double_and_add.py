#elliptic curve double and add algorithm
#computes n*P for some E (mod p), no more than 2log2(n) steps

import to_binary

def double_and_add(n,p,P,A):
    Q = P
    R = [float('inf'),float('inf')]

    for elem in to_binary(n)[::-1]:
        if elem == 1:
            R = elliptic_add_finite_field(R,Q,A,p)
        Q = elliptic_add_finite_field(Q,Q,A,p)

    return print(Q, R, elem)

double_and_add(947,3623,[6,730],14)
#Elliptic Curve addition over a finite field
# E: Y**2 = (x**3 + A*x + B) (mod p)

#add in discriminant condition

def elliptic_add_finite_field(p_1, p_2, A, p):

    if p_1[0] == float('inf') and p_1[1] == float('inf'):
        return p_2

    if p_2[0] == float('inf') and p_1[1] == float('inf'):
        return p_1

    if p_1[0] == p_2[0] and p_1[1] == -p_2[1]:
        return [float('inf'), float('inf')]

    else:
        if p_1 != p_2:

            y = (p_2[1] - p_1[1]) % p
            x = (p_2[0] - p_1[0]) % p
            x_inv = pow(x, -1, p)
            lbda = (y * x_inv) % p
            v = (p_1[1] - lbda * p_1[0]) % p

        if p_1 == p_2:

            y = (3 * p_1[0] ** 2 + A) % p
            x = (2 * p_1[1]) % p
            x_inv = pow(x, -1, p)
            lbda = (y * x_inv) % p
            v = (p_1[1] - lbda * p_1[0]) % p

        x_3 = (lbda ** 2 - p_1[0] - p_2[0]) % p
        y_3 = -(lbda * x_3 + v) % p
        p_3 = [x_3, y_3]

        return p_3

    return None

p_1,p_2 = [0,0], [6,730]
A = 3
p=13
elliptic_add_finite_field(p_1,p_2,A,p)
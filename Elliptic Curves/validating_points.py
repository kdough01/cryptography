#Finding valid points on an elliptic curve over a finite field
# E: Y**2 = (x**3 + a*x + b) (mod p)

import math as m

def elliptic_points(a, b, p):

    points = {}
    for x in range(1, p):
        y = (x ** 3 + a * x + b) % p

        for y_2 in range(1, p):
            if pow(y_2, 2, p) == y:
                if x in points:
                    points[x].append(y_2)
            else:
                points[x] = [y_2]

    points[float('inf')] = float('inf')

    return points

elliptic_points(3,8,13)
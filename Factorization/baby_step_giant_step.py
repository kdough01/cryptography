import math as m

def baby_step_giant_step(h, p, g = 2):
    """
    This is a function for the Babystep Giantstep Algorithm.
    It solves the discrete log problem g^x = h in O(sqrt(N) * log(N))
    steps with O(sqrt(N)) storage.

    Parameters
    h : int - the target value (h in the equation g^x = h mod p)
    p : int - a prime number representing the modulus
    g : int - the base (default is 2)
    """
    # Calculate N, whenever we do something N times it is essentially sqrt(p-1) times
    N = int(m.ceil(m.sqrt(p-1)))
    #print(f"N={N}")

    """
    Create a dictionary to store the baby steps.
    Compute (g ^ i) mod p for i in the range [0, N) and store them in the dictionary.
    The key is the result of (g ^ i) mod p and the value is i.
    """
    t = {}
    for i in range(N):
        t[pow(g,i,p)] = i
    print(t) # Print just to show the dicionary

    """
    Compute c = g ^ (-N) mod p using Fermat's Little Theorem.
    g ^ (-N) = g ^ (-N * (p - 2)) mod p because g ^ (p - 1) = 1 mod p
    """
    c = pow(g,N*(p-2),p)

    """
    Iterate over the giant steps.
    We compute (h * g^(-jN)) mod p for j in the range [0, N).
    If this matches any value in the baby step table we have found our solution.
    """
    for j in range(N):
        y = (h * pow(c, j, p)) % p
    if y in t:
        return j*N+t[y]

    return None

# Example usage
baby_step_giant_step(22,53,5)
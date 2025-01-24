import random
import math

class rsa():

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def encrypt(self, message):
        n = self.p * self.q
        e_list = []
        n_1 = (self.p - 1) * (self.q - 1)

        for i in range(2, n_1):
            if math.gcd(int(i), n_1) == 1:
                e_list.append(i)

        e = random.choice(e_list)
        encrypted_message = (message ** e) % n
        print(e_list)

        return e

    def decrypt(self, e):
        n_1 = (self.p - 1) * (self.q - 1)
        n_2 = self.p * self.q

        d = pow(e, -1, n_1)

        message = (e ** d) % n_2

        return message
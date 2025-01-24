#Congruential Key

def congruential_key_creation(q,f,g):
    if (f < np.sqrt(q/2)) and (np.sqrt(q/4) < g < np.sqrt(q/2)) and (math.gcd(f,q*g) == 1):
        f_inv = pow(f,-1,q)
        h = (f_inv*g)%q
        return [q,h]
    else:
        print('Make sure f < sqrt(q/2), sqrt(q/4) < g < sqrt(q/2), and gcd(f,q*g) = 1.')

def congruential_encryption(r,m,q):
    h = congruential_key_creation(q,f,g)[1]
    if 0 < m < np.sqrt(q/4) and 0 < r < np.sqrt(q/2):
        e = (r*h + m)%q
        return e
    else:
        print('Choose an m between 0 and sqrt(q/4) and an r between 0 and sqrt(q/2).')

def congruential_decryption(f,q,g):
    e = congruential_encryption(r,m,q)
    a = (f*e)%q
    f_inv = pow(f,-1,g)
    b = (f_inv*a)%g
    return b

q = 122430513841
f = 231231
g = 195698

m = 123456
r = 101010

print(congruential_key_creation(q,f,g))
print(congruential_encryption(r,m,q))
print(congruential_decryption(f,q,g))
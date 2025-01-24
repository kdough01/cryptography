#Subset Sum
import numpy as np
import math

def subset_sum_key_creation(r,A,B):

    if B>2*r[-1] and math.gcd(A,B)==1:
        M = []
        
    for elem in range(len(r)):
        M.append((A*r[elem])%B)
    return M

def subset_sum_encryption(x):
    S = np.dot(np.array(x),subset_sum_key_creation(r,A,B))
    return S

def subset_sum_decryption(A,B,r):

    A_inv = pow(A,-1,B)
    S = subset_sum_encryption(x)
    S_prime = (A_inv*subset_sum_encryption(x))%B
    X = []
    r = r[::-1]

    for elem in range(len(r)):
        if S_prime >= r[elem]:
            X.append(1)
            S_prime-=r[elem]
        else:
            X.append(0)
    return X[::-1]

r = [3,11,24,50,115]
A = 113
B = 250
x = [1,0,1,0,1]

print(subset_sum_key_creation(r,A,B))
print(subset_sum_encryption(x))
print(subset_sum_decryption(A,B,r))
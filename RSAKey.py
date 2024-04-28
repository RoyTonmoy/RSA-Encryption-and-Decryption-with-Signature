import random
import math

primes = []

for possiblePrime in range(32768, 40001):
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    if isPrime:
        primes.append(possiblePrime)


def isPEqualQ(p, q):
    if p == q:
        num = random.choice(primes)
        q = num


def selecting_e(phi):
    num = math.ceil(phi/11001)
    e = random.randint(1, num)
    g = math.gcd(e, phi)
    while g != 1:
        print("checking e")
        e = random.randint(1, num)
        g = math.gcd(e, phi)
    
    if e < phi:
        return e
        
def extended_gcd(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
    return (g, x - (b // a) * y, y)


def getPrivateKey(e, phi_n):
    d = extended_gcd(e, phi_n)[1]
    d = d % phi_n

    if d < 0:
        d += phi_n
    return d


p = random.choice(primes)
q = random.choice(primes)
isPEqualQ(p, q)

N = p * q
PhiOf_N = (p - 1) * (q - 1)
e = selecting_e(PhiOf_N)
d = getPrivateKey(e, PhiOf_N)


print("Prime p: ", p)
print("Prime q: ", q)
print("N: ", N)
print("Phi_N: ", PhiOf_N)
print("Public key e: ", e)
print("Private key d =",d)





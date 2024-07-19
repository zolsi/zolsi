
# Python for RSA asymmetric cryptographic algorithm.

import math


def gcd(a, h):
	tempo = 0
	while(1):
		tempo = a % h
		if (tempo == 0):
			return h
		a = h
		h = tempo


p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)

while (e < phi):

	# e must be co-prime to phi and
	# smaller than phi as RSA algorithm defined .
	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1

# choosing d such that it satisfies
# d*e = 1 + k * totient or euler function can be called it count the 

k = 2
d = (1 + (k*phi))/e

# Message to be encrypted
msg = 14.0

print("Message data = ", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted data = ", c)

# Decryption m = (c ^ d) % n
m = pow(c, d)
m = math.fmod(m, n)
print("Original Message Sent = ", m)

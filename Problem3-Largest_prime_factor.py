# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

prime_factors = []

for i in range(600851475143):
    if 600851475143 % i == 0:
        prime_factors.append(i)

print(prime_factors)

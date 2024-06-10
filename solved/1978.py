num = int(input())
input = input().split()

for i in range(num):
    input[i] = int(input[i])

# function that checks if a number is prime
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primes = 0
for i in input:
    if isPrime(i) == True:
        primes += 1

print(primes)
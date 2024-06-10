import math
a = input().split()

# Convert to Int

a = list(map(int, a))
    
print(math.gcd(a[0], a[1]))
print(math.lcm(a[0], a[1]))

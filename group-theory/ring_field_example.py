"""
Rings and fields: integers mod 5
"""
mod = 5
ring = [x for x in range(mod)]
field = [x for x in range(1, mod) if math.gcd(x, mod) == 1]
print("Ring Z_5:", ring)
print("Field Z_5^*:", field)

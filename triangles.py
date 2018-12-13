import math
a = int(input("Enter a length for your first leg."))
b = int(input("Enter a length for your second leg."))

def pythagorean(a,b):
  c = math.sqrt((a*a)+(b*b))
  return c

print(pythagorean(a,b))

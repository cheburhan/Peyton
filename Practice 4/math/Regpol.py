import math
n = int(input())
side = float(input())
area = (n * side**2) / (4 * math.tan(math.pi / n))
print(int(area))

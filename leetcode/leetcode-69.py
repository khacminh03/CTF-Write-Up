import math
def mySqrt(self, x):
        result = math.sqrt(x)
        return int(math.floor(result))

num = int(input())
print(mySqrt(num))
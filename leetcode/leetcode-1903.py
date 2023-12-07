def largestOdd(num):
    for i in range(len(num) - 1, -1, -1):
        if (int(num[i]) % 2 == 1):
            return num[:i+1]
    return ""
num = str(input())
print(largestOdd(num))

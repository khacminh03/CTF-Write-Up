def addBinary(a, b):
    countA = 0
    countB = 0
    resultOfA = 0
    resultOfB = 0
    for char in reversed(a):
        resultOfA = resultOfA + (int(char) * (2 ** countA))
        countA += 1
    for char in reversed(b):
        resultOfB = resultOfB + (int(char) * (2 ** countB))
        countB += 1
    add = resultOfA + resultOfB
    result = bin(add)
    print(result[2 : len(result)])
a, b = input().split()
addBinary(a, b)
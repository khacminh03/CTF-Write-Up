def plusOne(digits):
    number = ""
    for item in digits:
        number = number + str(item)
    number = int(number) + 1
    final = []
    while(number != 0):
        temp = number % 10
        final.append(temp)
        number = number // 10
    return final[::-1]
    
digits = list(map(int, input().split()))
print(plusOne(digits))
def countBit(n):
    lst = []
    for i in range (0, n + 1):
        binary = bin(i)
        lst.append(binary[2:len(binary)])
    count = dict()
    for item in lst:
        temp = 0
        for char in item:
            if (char == "1"):
                temp += 1
        count[item] = temp
    result = []
    for item in count.values():
        result.append(item)
    print(result)
nums = int(input("Enter number: "))
countBit(nums)

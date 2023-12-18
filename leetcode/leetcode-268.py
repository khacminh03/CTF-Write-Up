def missingNumber(nums):
    nums = sorted(nums)
    arr = []
    result = 0
    for i in range (0, len(nums) + 1):
        arr.append(i)
    for item in arr:
        if (item not in nums):
            result = item
    print(result)
nums = list(map(int, input("Enter the list: ").split()))
missingNumber(nums)

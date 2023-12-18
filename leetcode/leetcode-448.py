def findDissappearedNumber(nums):
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])
        
    res = []
    for i, n in enumerate(nums):
        if (n > 0):
            res.append(i + 1)
    return res
nums = list(map(int, input("Enter the list: ").split()))
findDissappearedNumber(nums)
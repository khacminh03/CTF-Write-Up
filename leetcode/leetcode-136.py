def singleNumber(nums):
    count = dict()
    for item in nums:
        count[item] = count.get(item, 0) + 1
    
    for k in count.keys():
        if (count[k] == 1):
            print(k)
nums = list(map(int, input("Enter the list: ").split()))
singleNumber(nums)
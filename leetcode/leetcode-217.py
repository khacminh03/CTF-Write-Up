def containDuplicates(nums):
    count = dict()
    for num in nums:
        count[num] = count.get(num, 0) + 1
    dup = False
    for value in count.values():
         if (value > 1):
             dup = True
    return dup   
nums = list(map(int, input().split()))

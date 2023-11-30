def productExceptSelf(nums):
    product = 1
    for item in nums:
        product *= item
    
    result = []
    for item in nums:
        if (item != product):
            result.append(int(product / item))
        else:
            prod = 1
            for i in nums:
                if (i != item):
                    prod *= i
            result.append(prod)
    print(result)
nums = list(map(int, input().split()))
productExceptSelf(nums)
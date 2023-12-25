class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
    
    def sumRange(self, left, right):
        sum = 0
        for i in range(left, right + 1):
            sum = sum + self.nums[i]
        print(sum)
lst = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(lst)
numArray.sumRange(0, 2)
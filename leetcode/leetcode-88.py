def merge(nums1, m, nums2, n):
    for i in range (0, n):
            nums1[m] = nums2[i]
            m = m + 1
    
    for i in range (0, len(nums1)):
        for j in range (i + 1, len(nums1)):
            if (nums1[i] > nums1[j]):
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp
    print(nums1)
nums1 = list(map(int, input("Enter list 1: ").split()))
m = int(input("Enter m for list 1: "))
nums2 = list(map(int, input("Enter list 2: ").split()))
n = int(input("Enter n for list 2: "))
merge(nums1, m, nums2, n)

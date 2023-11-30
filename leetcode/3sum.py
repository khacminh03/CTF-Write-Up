def threeSum(nums):
    res = []
    nums.sort()  # Sắp xếp dãy số để giúp tìm các tổng dễ dàng hơn
    n = len(nums)

    for i in range(n - 2):
        # Loại bỏ trường hợp trùng lặp với số trước đó
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                # Loại bỏ trường hợp trùng lặp với số ở cả hai phía
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res

nums = list(map(int, input("Nhập danh sách số, cách nhau bằng dấu cách: ").split()))
threeSum(nums)

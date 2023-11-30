def topK(nums, k):
        count = dict()
        for item in sorted(nums):
            count[item] = count.get(item, 0) + 1
        sorted_dict = dict(sorted(count.items(), key = lambda item : item[1], reverse = True))
        result = list(sorted_dict.keys())
        final = []
        for i in range(0, k):
            final.append(result[i])
        return final
nums = list(map(int, input().split()))
k = int(input())
print(topK(nums, k))
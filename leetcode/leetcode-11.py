def container(array):
        res = 0
        l, r = 0, len(array) - 1

        while(l < r):
            area = (r - l) * min(array[l], array[r])
            res = max (res, area)

            if (array[l] < array[r]):
                l += 1
            else:
                r -= 1
        return res
array = list(map(int, input().split()))
container(array)
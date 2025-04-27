class Solution:
    def countLargestGroup(self, n: int) -> int:
        maxSize = 0
        sumSize = {}
        for i in range(1, n+1):
            sum = 0
            while i != 0:
                sum += i % 10
                i //= 10
            if sum not in sumSize:
                sumSize[sum] = []
            sumSize[sum].append(i)
            maxSize = max(maxSize, len(sumSize[sum]))
        res = 0
        for sum in sumSize:
            if len(sumSize[sum]) == maxSize:
                res += 1
        return res





        
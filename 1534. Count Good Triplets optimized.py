class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        maxValue = 0
        for i in range(len(arr)):
            maxValue = max(maxValue, arr[i])
        prefixCount = [0]*(maxValue+1)
        res = 0
        for j in range(len(arr)-1):
            for k in range(j+1, len(arr)):
                if abs(arr[j]-arr[k]) <= b:
                    right = min(arr[j] + a, arr[k] + c)
                    left = max(arr[j] - a, arr[k] - c)
                    left = max(left, 0)
                    right = min(right, maxValue)
                    
                    if left <= right:
                        res += prefixCount[right] - (0 if left == 0 else prefixCount[left-1])

            for index in range(arr[j], maxValue+1):
                prefixCount[index] += 1           
                   
        return res



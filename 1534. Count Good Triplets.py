class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j]) > a:
                    continue
                for k in range(j+1, len(arr)):
                    if abs(arr[j]-arr[k]) > b:
                        continue
                    if abs(arr[i]-arr[k]) > c:
                        continue
                    count += 1
        return count


        
# 1) iterate from 0 to len(arr) with i
# 2) iterate from i + 1 to len(arr) with j
#     check if difference with any of these is less then a
# 3) iterate from j + 1 to len(arr) with k
#     check if difference with any of these is less then b
#     check if difference with any of these is less then c

# O(n^3) is the time complexity
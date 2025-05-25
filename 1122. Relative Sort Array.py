class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = [0]*1001
        for num in arr1:
            freq[num] += 1
        res = []
        for num in arr2:
            while freq[num]:
                res.append(num)
                freq[num] -= 1
        for i in range(1001):
            while freq[i]:
                res.append(i)
                freq[i] -= 1
        return res
            
                
        
        
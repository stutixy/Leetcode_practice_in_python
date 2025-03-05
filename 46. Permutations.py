class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(indexSet, subSet):
            for i in range(n):
                if i in indexSet:
                    continue
                if len(subSet)+1 < n:
                    indexSet.add(i)
                    backtrack(indexSet, subSet + [nums[i]])
                    indexSet.remove(i)
                elif len(subSet)+1 == n:
                    result.append(subSet + [nums[i]])

        n = len(nums)
        result = []
        backtrack(set(), [])
        return result

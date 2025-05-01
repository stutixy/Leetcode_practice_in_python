class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            string = str(num)
            if len(string) % 2 == 0:
                count += 1
        return count
        
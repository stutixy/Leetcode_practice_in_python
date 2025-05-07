class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == answer:
                count += 1
            else:
                if count == 0:
                    answer = nums[i]
                else:
                    count -= 1
        return answer

class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        left = 0
        right = len(sList)-1
        while left < right:
            temp = sList[left]
            sList[left] = sList[right]
            sList[right] = temp
            left += 1
            right -= 1
        return " ".join(sList)

        
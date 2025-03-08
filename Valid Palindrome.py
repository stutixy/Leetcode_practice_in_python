class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<=j:
            if ord(s[i]) < 48 or (ord(s[i]) > 57 and ord(s[i]) < 65) or (ord(s[i]) > 90 and ord(s[i]) < 97) or ord(s[i]) > 122:
                i += 1
                
            elif ord(s[j]) < 48 or (ord(s[j]) > 57 and ord(s[j]) < 65) or (ord(s[j]) > 90 and ord(s[j]) < 97) or ord(s[j]) > 122:
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True 
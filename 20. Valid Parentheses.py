class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookupBracket = {"[":"]", "{":"}", "(":")"}
        pointer = 0
        while pointer < len(s):
            if s[pointer] is "}" or s[pointer] is "]" or s[pointer] is ")":
                if not stack:
                    return False
                top = stack.pop()
                if lookupBracket[top] is not s[pointer]:
                    return False
            else:
                stack.append(s[pointer])
            pointer += 1
        if stack:
            return False
        return True
                    
            
             

        
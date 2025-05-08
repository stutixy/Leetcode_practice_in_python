class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        lookup = {0:"", 1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        return self.helper([], digits, 0, [], lookup)

    def helper(self, current, digits, i, result, lookup):
        
        if i>= len(digits):
            final = ''.join(current)
            result.append(final)
        else:
            for letter in lookup[int(digits[i])]:
                current.append(letter)
                result = self.helper(current, digits, i+1, result, lookup)
                current.pop()
                    
        return result
        
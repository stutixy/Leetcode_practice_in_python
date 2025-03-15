class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lookup = {}
        minLenWord = words[0]
        minLen = float('inf')
        for word in words:
            if len(word) < minLen:
                minLen = len(word)
                minLenWord = word
        words.remove(minLenWord)

        for c in minLenWord:
            if c not in lookup:
                lookup[c] = 0
            lookup[c] += 1
        
        currentWordSet = {}
        
        for word in words:
            currentWordSet.clear()
            for c in word:
                if c not in currentWordSet:
                    currentWordSet[c] = 0
                currentWordSet[c] += 1

            for key in lookup:
                if key not in currentWordSet:
                    lookup[key] = 0
                else:
                    lookup[key] = min(lookup[key], currentWordSet[key])
       
        result = []
        for key in lookup:
            while lookup[key] > 0:
                result.append(key)
                lookup[key] -= 1
        return result

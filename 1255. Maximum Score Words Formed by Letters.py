class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = Counter(letters)

        def dfs(i):
            if i == len(words):
                return 0
            word = words[i]
            
            wordFreq = {}
            for l in word:
                wordFreq[l] = 1 + wordFreq.get(l, 0)

            canBeFormed = True

            for l in wordFreq:
                if freq.get(l,0) < wordFreq[l]:
                    canBeFormed = False
                    break

            curr_score = 0

            if canBeFormed:
                for l in wordFreq:
                    freq[l] -= wordFreq[l]
                    curr_score += (wordFreq[l] * score[ord(l) - ord('a')])
                
                curr_score += dfs(i+1)
            
                for l in wordFreq:
                    freq[l] += wordFreq[l]
                    
            return max(curr_score, dfs(i+1))
    
        return dfs(0)
                
                


        
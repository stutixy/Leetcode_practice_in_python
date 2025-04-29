class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        wordSet = set(wordList)
        while queue:
            currentWord, distance = queue.popleft()
            if currentWord == endWord:
                return distance
            for i in range(len(currentWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = currentWord[:i] + c + currentWord[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append([newWord, distance+1])
        return 0
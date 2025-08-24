class Trie:

    def __init__(self):
        self.root = {}
        self.endSymbol = '*'
        

    def insert(self, word: str) -> None:
        current = self.root
        for j in range(len(word)):
            letter = word[j]
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = True


    def search(self, word: str) -> bool:
        current = self.root
        for l in word:
            if l in current:
                current = current[l]
            else:
                return False
        if self.endSymbol in current:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for l in prefix:
            if l in current:
                current = current[l]
            else:
                return False
        return True
        

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
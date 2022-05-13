class Node:
    def __init__(self):
        self.st = [None for i in range(26)]
        self.flag = False
        
    
class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        for ch in word:
            if curr.st[ord(ch)-ord("a")] == None:
                curr.st[ord(ch) - ord("a")] = Node()
            curr = curr.st[ord(ch) - ord("a")]
        
        curr.flag = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for ch in word:
            if curr.st[ord(ch) - ord("a")] == None:
                return False
            curr = curr.st[ord(ch) - ord("a")]
        
        return curr.flag
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for ch in prefix:
            if curr.st[ord(ch) - ord("a")] == None:
                return False
            curr = curr.st[ord(ch) - ord("a")]
        
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
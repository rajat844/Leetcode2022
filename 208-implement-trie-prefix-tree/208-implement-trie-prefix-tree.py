class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
        
    def isContains(self,ch):
        if self.links[ord(ch) - ord('a')] == None:
            return False
        return True
        
    def put(self,ch,node):
        self.links[ord(ch) - ord('a') ] = node
        
    def get(self,ch):
        return self.links[ord(ch) - ord('a')]
    
    def markEnd(self):
        self.flag = True
        
    def isEnd(self):
        return self.flag

class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        node = self.root
        
        for i in range(len(word)):
            if not node.isContains(word[i]):
                node.put(word[i],TrieNode())
            node = node.get(word[i])
        
        node.markEnd()

    def search(self, word: str) -> bool:
        node  = self.root
        
        for i in range(len(word)):
            if not node.isContains(word[i]):
                return False
            node = node.get(word[i])
            
        return node.isEnd()
        

    def startsWith(self, prefix: str) -> bool:
        node  = self.root
        
        for i in range(len(prefix)):
            if not node.isContains(prefix[i]):
                return False
            node = node.get(prefix[i])
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
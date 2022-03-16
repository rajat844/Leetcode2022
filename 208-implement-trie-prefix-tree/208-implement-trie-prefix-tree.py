class Node:
    def __init__(self):
        self.st = [None for i in range(26)]
        self.flag = False
        
    def isContain(self,ch):
        return self.st[ord(ch) - ord('a')] != None
    
    def put(self,ch):
        self.st[ord(ch) - ord('a')] = Node()
        
    def get(self,ch):
        return self.st[ord(ch) - ord('a')] 
    
    def end(self):
        self.flag = True
        
    def isEnd(self):
        return self.flag
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not node.isContain(word[i]):
                node.put(word[i])
            node = node.get(word[i])
            
        node.end()

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if not node.isContain(word[i]):
                return False
            node = node.get(word[i])
            
        return node.isEnd()
           

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if not node.isContain(prefix[i]):
                return False
            node = node.get(prefix[i])
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class TrieNode:
    def __init__(self):
        self.links = [None]*26 
        self.flag = False
        
    def containsKey(self,ch):
        uni = ord(ch)
        return self.links[uni - 97] != None
    
    def put(self,ch,node):
        uni = ord(ch)
        self.links[uni - 97] = node
        
    def get(self,ch):
        uni = ord(ch)
        return self.links[uni - 97]
    
    def setEnd(self):
        self.flag = True
        
    def isEnd(self) -> bool:
        return self.flag
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        
        for i in range(len(word)):
            if node.containsKey(word[i]) == False:
                node.put(word[i],TrieNode())
            node = node.get(word[i])
                
        node.setEnd()
        

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if node.containsKey(word[i]) == False:
                return False
            node = node.get(word[i])
            
        if node.isEnd() == True:
            return True
        return False
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if node.containsKey(prefix[i]) == False:
                return False
            node = node.get(prefix[i])
            
        return True
                
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
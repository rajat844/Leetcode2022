class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self,word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        
        curr.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
        
        rows,columns = len(board),len(board[0])
        res,visited = set(),set()
        
        def helper(r,c,node,word):
            if r < 0 or c < 0 or r == rows or c == columns or  (r,c) in visited or board[r][c] not in node.children:
                return 
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord:
                res.add(word)
            
            helper(r+1,c,node,word)
            helper(r-1,c,node,word)
            helper(r,c+1,node,word)
            helper(r,c-1,node,word)
            
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(columns):
                helper(r,c,root,"")
        
        return list(res)
                
                
                
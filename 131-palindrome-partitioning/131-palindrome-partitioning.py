class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def helper(start,path):
            if start == len(s):
                ans.append(path)
                return
            for end in range(start+1,len(s)+ 1):
                sub = s[start:end]
                if sub == sub [::-1]:
                    helper(end,path+[sub])
        helper(0,[])
        return ans
                
        
        
        
        
        
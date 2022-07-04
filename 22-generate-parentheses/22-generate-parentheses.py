class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(i,j,s):
            if i > n:
                return 
            if i == n and j == n:
                ans.append(s)
                return
            if i == j:
                generate(i+1,j,s+"(")
            else:
                generate(i+1,j,s+"(")
                generate(i,j+1,s+")")
            
        ans = []
        generate(0,0,"")
        return ans
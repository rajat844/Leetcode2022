class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(op,cl,s):
            if op < 0:
                return 
            if op == 0 and cl == 0:
                ans.append(s[::])
                return
            if op == cl:
                generate(op-1,cl,s+"(")
            elif op < cl:
                generate(op-1,cl,s+"(")
                generate(op,cl-1,s+")")
        ans = []
        generate(n,n,"")
        return ans
        
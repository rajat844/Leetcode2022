class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def helper(i,s):
            if i == len(digits):
                if len(s) > 0:
                    ans.append(s[::])
                return
            
            x = dic[digits[i]]
            for j in range(len(x)):
                helper(i+1,s+x[j])
        ans = []
        helper(0,'')
        return ans
            
            
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack,match = [] , {'}' : '{' , ')' : '(' ,']' : '[' }
        
        for i in s:
            if i in match:
                if not (stack and stack.pop() == match[i]):
                    return False
            else:
                stack.append(i)
                
        return not stack
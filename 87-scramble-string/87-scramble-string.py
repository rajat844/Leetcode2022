class Solution:
    def __init__(self):
        self.dic = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1,s2) in self.dic:
            return self.dic[(s1,s2)]
        
        if len(s1) != len(s2):
            self.dic[(s1,s2)] = False
            return self.dic[(s1,s2)]
        
        if s1 == s2:
            self.dic[(s1,s2)] = True
            return self.dic[(s1,s2)]
        
        if sorted(s1) != sorted(s2):
            self.dic[(s1,s2)] = False
            return self.dic[(s1,s2)]
        
        for i in range(1, len(s1)):
            cndn1 = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
            cndn2 = self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])
            if cndn1 or cndn2:
                self.dic[(s1,s2)] = True
                return self.dic[(s1,s2)]
        self.dic[(s1,s2)] = False
        return self.dic[(s1,s2)]
        
        
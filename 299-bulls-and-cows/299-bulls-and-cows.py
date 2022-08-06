class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s = list(secret)
        g = list(guess)
        
        st1 = defaultdict(int)
        st2 = defaultdict(int)
        bulls = 0
        for i in range(len(g)):
            if s[i] == g[i]:
                bulls += 1
                s[i] = ""
                g[i] = ""

            else :
                st1[s[i]] += 1
                st2[g[i]] += 1
        
        cows = 0
        for x in st2:
            if x in st1:
                cows += min(st1[x],st2[x])
        
        return "".join([str(bulls),"A",str(cows),"B"])
        
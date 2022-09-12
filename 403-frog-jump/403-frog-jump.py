class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def recursion(curr,speed):
            if (curr,speed) in st:
                return False
            if curr == stones[-1]:
                return True
            
            if curr > stones[-1] or curr < 0 or speed <= 0 or curr not in stones:
                return False
            
            cases = [speed-1,speed,speed+1]
            
            for x in cases:
                if x + curr in stones:
                    if recursion(curr+x,x):
                        return True
                    
            st.add((curr,speed))
            return False
        
        st = set()
        return recursion(1,1)
                    
            
            
        
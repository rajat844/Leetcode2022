class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = (k*(k+1))//2
        st = set()
        cnt = 0
        
        for x in nums:
            if x not in st and x <= k:
                ans -= x
                cnt += 1
            st.add(x)
            
        while cnt > 0:
            if k+1 not in st:
                ans += k+1
                cnt -= 1
            k = k+1
        
        return ans
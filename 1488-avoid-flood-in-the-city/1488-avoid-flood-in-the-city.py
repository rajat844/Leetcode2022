from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        mp = {}
        st = SortedList()
        ans = [1 for i in range(len(rains))]
        
        for i in range(len(rains)):
            if rains[i] == 0:
                st.add(i)
            else:
                if rains[i] in mp:
                    x = bisect.bisect_right(st,mp[rains[i]])
                    if x < len(st):
                        ans[st[x]] = rains[i]
                        st.remove(st[x])
                    else:
                        return []
                mp[rains[i]] = i
                ans[i] = -1
        
        return ans
                
                    
        
        
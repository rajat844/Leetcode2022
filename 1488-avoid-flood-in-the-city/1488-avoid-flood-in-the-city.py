from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        mp = {}
        st = SortedList()
        ans = [1 for i in range(len(rains))]

        for i in range(len(rains)):
            if rains[i] == 0:
                st.add(i)
            elif rains[i] > 0:
                if rains[i] in mp:
                    a = bisect.bisect_right(st,mp[rains[i]])
                    if a < len(st):
                        ans[st[a]] = rains[i]
                        st.remove(st[a])
                    else:
                        return []
                ans[i] = -1
                mp[rains[i]] = i
        
        for i in range(len(ans)):
            if ans[i] == 0:
                ans[i] = 1
        
        return ans
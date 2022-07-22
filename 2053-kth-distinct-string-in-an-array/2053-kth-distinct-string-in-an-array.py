from collections import defaultdict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        st = defaultdict(int)
        
        for i in range(len(arr)):
            st[arr[i]] += 1
        
        for x in st:
            if st[x] == 1:
                k -= 1
                if k == 0:
                    return x
        
        return ""
        
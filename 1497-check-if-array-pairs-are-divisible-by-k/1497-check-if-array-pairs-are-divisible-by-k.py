class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        st  = [0 for i in range(k)]
        for i in range(len(arr)):
            arr[i] %= k
            if arr[i] < 0 :
                arr[i] += k
            st[arr[i]] += 1
        
        if st[0] % 2 != 0:
            return False
        
        for i in range(1,(k//2)+1):
            if st[i] != st[k-i]:
                return False
            
        return True
            
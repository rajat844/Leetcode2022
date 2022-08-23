class Solution:
    def minDeletions(self, s: str) -> int:
        st = Counter(s)
        arr = []
        for x in st:
            arr.append(st[x])
        
        arr.sort(reverse = True)
        
        mx = math.inf
        ans = 0
        
        for i in range(len(arr)):
            if mx == 0:
                ans += arr[i]
            elif arr[i] > mx:
                ans += arr[i] - mx
                mx -= 1
            else :
                mx = arr[i] - 1
        
        return ans
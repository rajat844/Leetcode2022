class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        h = {}
        for i in arr:
            h[i] = h.get(i,0)+1
        vals = []
        for i in h.keys():
            vals.append([i,h[i]])
        vals.sort(key=lambda x:x[1],reverse=True)
        size = 0
        i = 0
        while i < len(vals) and size < len(arr)//2:
            size += vals[i][1]
            i += 1
        return i
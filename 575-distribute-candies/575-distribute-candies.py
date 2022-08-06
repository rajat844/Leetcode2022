class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        st = defaultdict(int)
        for i in range(len(candyType)):
            st[candyType[i]] += 1
        
        x = len(candyType)//2
        n = len(st)
        
        for typ in st:
            x = x - st[typ] + 1
        
        if x <= 0:
            return n
        return n - x
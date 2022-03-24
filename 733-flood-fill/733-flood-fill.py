class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        def helper(sr,sc):
            if sr < 0 or sr >= n or sc < 0 or sc >= m or image[sr][sc] != source:
                return 
            
            image[sr][sc] = newColor
            
            helper(sr-1,sc)
            helper(sr,sc-1)
            helper(sr+1,sc)
            helper(sr,sc+1)
        
                
        source = image[sr][sc]
        n = len(image)
        m = len(image[0])
        helper(sr,sc)
        return image
        
        
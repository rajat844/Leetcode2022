class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        st = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                st[i-j].append(mat[i][j])
                
        for x in st:
            st[x].sort(reverse = True)
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = st[i-j].pop()

        return mat
        
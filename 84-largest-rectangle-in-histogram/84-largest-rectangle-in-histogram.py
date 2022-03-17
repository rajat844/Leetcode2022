class Solution:
    def largestRectangleArea(self, num: List[int]) -> int:
        left_smaller = []
        right_smaller = []
        st = []
        
        for i in range(len(num)):
            while len(st) > 0 and num[i] <= num[st[-1]]:
                st.pop()
            
            if len(st) == 0:
                left_smaller.append(0)
            else :
                left_smaller.append(st[-1] + 1)
            
            st.append(i)
            
        st.clear()
        
        for i in range(len(num)-1,-1,-1):
            while len(st) > 0 and num[i] <= num[st[-1]]:
                st.pop()
            
            if len(st) == 0:
                right_smaller.append(len(num) - 1)
            else:
                right_smaller.append(st[-1] -1)
            
            st.append(i)
            
        right_smaller = right_smaller[::-1]
        
        ans = 0
        for i in range(len(num)):
            ht = num[i]
            wt = right_smaller[i] - left_smaller[i] + 1
            h = ht*wt
            ans = max(h,ans)
            
        return ans
            
            
            
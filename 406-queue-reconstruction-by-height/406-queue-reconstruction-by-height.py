class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def mycmp(a,b):
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            elif a[0] == b[0]:
                if a[1] > b[1]:
                    return 1
                elif a[1] < b[1]:
                    return -1
                else:
                    return 0
            else:
                return 0
            
        n = len(people)
        people.sort(key = cmp_to_key(mycmp))
        ans = [None for i in range(n)]
        
        for i in range(n):
            cnt = people[i][1]
            for j in range(n):
                if cnt == 0 and ans[j] == None:
                    ans[j] = people[i]
                    break
                elif ans[j] == None or ans[j][0] >= people[i][0]:
                    cnt -= 1
        
        return ans
                
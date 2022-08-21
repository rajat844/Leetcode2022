class Solution:
    def movesToStamp(self, s: str, t: str) -> List[int]:
        def canChange(i):
            a = 0
            for j in range(i,i+len(stamp)):
                if target[j] == None or target[j] == stamp[a]:
                    a += 1
                else:
                    return False
            
            return True
        
        def changeTarget(i):
            cnt = 0
            for j in range(i,i+len(stamp)):
                if target[j] != None:
                    target[j] = None
                    cnt += 1
            return cnt
        
        stamp = [i for i in s]
        target = [i for i in t]
        
        ans = []
        cnt = 0
        visited = [False for i in range(len(target))]
        
        while cnt != len(target):
            change = False
            for i in range(len(target) - len(stamp) + 1):
                if visited[i] == False and canChange(i):
                    cnt += changeTarget(i)
                    visited[i] = True
                    change = True
                    ans.append(i)
                    
                    if cnt == len(target):
                        break
            
            if change == False:
                return []
        
        return ans[::-1]
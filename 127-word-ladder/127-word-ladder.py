from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        
        if endWord not in words:
            return 0
        
        que = deque()
        que.append(beginWord)
        
        ans = 1
        while len(que) > 0:
            k = len(que)
            while k > 0:
                k -= 1
                curr = que.popleft()
                for i in range(len(curr)):
                    temp = curr
                    for j in range(97,123):
                        temp = temp[:i]+ chr(j) + temp[i+1:]
                        if temp == curr:
                            continue
                        elif temp == endWord:
                            return ans+1
                        elif temp in words:
                            que.append(temp)
                            words.remove(temp)
            ans += 1
        return 0
                
                    
            
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = []
        self.iterator = -1
        self.simplify(nestedList)
        
    def simplify(self,lst):
        for i in range(len(lst)):
            if lst[i].isInteger() == True:
                self.st.append(lst[i].getInteger())
            else:
                x = lst[i].getList()
                self.simplify(x)
    
    def next(self) -> int:
        self.iterator += 1
        return self.st[self.iterator]
    
    def hasNext(self) -> bool:
        if self.iterator == len(self.st) -1 :
            return False
        return True
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
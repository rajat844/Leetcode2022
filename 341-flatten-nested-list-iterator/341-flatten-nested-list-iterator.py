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
    def helper(self,nestedList):
        for i in range(len(nestedList)):
            if nestedList[i].isInteger() == True:
                self.st.append(nestedList[i].getInteger())
            else:
                x = nestedList[i].getList()
                self.helper(x)
    def __init__(self, nestedList: [NestedInteger]):
        self.st = []
        self.helper(nestedList)
        self.ps = -1

    def next(self) -> int:
        self.ps += 1
        return self.st[self.ps]

    
    def hasNext(self) -> bool:
        if len(self.st)-1 == self.ps:
            return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
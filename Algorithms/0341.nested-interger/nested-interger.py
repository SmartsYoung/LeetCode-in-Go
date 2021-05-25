# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
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

from collections import deque


class NestedIterator(object):
    def __init__(self, nestedList):
        self.q = deque()
        for li in nestedList:  # 先把所有的都放到队列中，然后在hasNext方法中依次展开
            self.q.append(li)

    def next(self):
        return self.q.popleft().getInteger()

    def hasNext(self):
        while self.q and self.q[0].isInteger() == False:
            tempLi = self.q.popleft().getList()  # 队列中第一个是列表，把他弹出并展开在放到队列里
            for i in tempLi[::-1]:  # 倒序放
                self.q.appendleft(i)  # 从队列头倒着放
        return len(self.q) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

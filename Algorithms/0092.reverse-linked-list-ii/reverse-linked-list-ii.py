# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

solution = Solution()

def test_reverseBetween1():
    head = ListNode.stringToListNode("[1,2,3,4,5]")
    m = 2
    n = 4
    expect = "[1, 4, 3, 2, 5]"
    actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
    assert actual == expect


def test_reverseBetween2():
    head = ListNode.stringToListNode("[1,2,3,4,5]")
    m = 5
    n = 5
    expect = "[1, 2, 3, 4, 5]"
    actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
    assert actual == expect


def test_reverseBetween3():
    head = ListNode.stringToListNode("[1,2,3,4,5]")
    m = 1
    n = 1
    expect = "[1, 2, 3, 4, 5]"
    actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
    assert actual == expect


def test_reverseBetween4():
    head = ListNode.stringToListNode("[1,2,3,4,5]")
    m = 1
    n = 3
    expect = "[3, 2, 1, 4, 5]"
    actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
    assert actual == expect


def test_reverseBetween5():
    head = ListNode.stringToListNode("[1,2,3,4,5,6,7,8,9]")
    m = 1
    n = 5
    expect = "[5, 4, 3, 2, 1, 6, 7, 8, 9]"
    actual = ListNode.listNodeToString(solution.reverseBetween(head, m, n))
    assert actual == expect


if __name__ == '__main__':
    test_reverseBetween1()
    test_reverseBetween2()
    test_reverseBetween3()
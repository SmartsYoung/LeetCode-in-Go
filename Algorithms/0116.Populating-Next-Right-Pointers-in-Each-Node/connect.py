class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_two_nodes(self, l: Node, r: Node):
            if l is None or r is None:
                return
            l.next = r

            self.connect(l.left, l.right)
            self.connect(r.left, r.right)
            self.connect(l.right, r.left)

        if root is None:
            return None
        self.connect_two_nodes(root.left, root.right)
        return root



class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, node):
        if node == None:
            return node
        if node.next == None:
            return node
        node1 = self.solve(node.next)
        node.next.next = node
        node.next = None
        return node1


node = LLNode(0, LLNode(1))

print(Solution().solve(node))

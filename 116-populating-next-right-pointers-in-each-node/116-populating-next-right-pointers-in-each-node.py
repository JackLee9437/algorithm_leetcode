"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root :
            return root
        
        que = deque([(root, 0)])
        while que :
            node, level = que.popleft()
            if que and que[0][1] == level :
                node.next = que[0][0]
            
            if node.left :
                que.append((node.left, level+1))
            if node.right :
                que.append((node.right, level+1))
        
        return root
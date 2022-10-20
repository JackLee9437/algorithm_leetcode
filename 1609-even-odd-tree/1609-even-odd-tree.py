# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([(root, 0)])
        level = -1
        prev = 0
        while que :
            node, l = que.popleft()
            if (l & 1 and node.val & 1) or (not l & 1 and not node.val & 1) :
                return False
            if level != l :
                level = l
                prev = node.val
            else :
                if level & 1 :
                    if prev <= node.val :
                        return False
                    prev = node.val
                else :
                    if prev >= node.val :
                        return False
                    prev = node.val
            
            if node.left :
                que.append((node.left, l+1))
            if node.right :
                que.append((node.right, l+1))
        
        return True
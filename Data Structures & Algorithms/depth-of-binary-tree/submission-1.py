# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            for i in range(len(q)):
                p = q.popleft()
                if p:
                    level.append(p.val)
                    q.append(p.left)
                    q.append(p.right)
            if level:
                depth +=1
        return depth
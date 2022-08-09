# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        
        while q:
            rightSide = None
            qlen = len(q)
            
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    # add child nodes of the current level
                    # in the queue for the next level
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightSide:
                # The current level is finished.
                # Its last element is the rightmost one.
                res.append(rightSide.val)
                
        return res
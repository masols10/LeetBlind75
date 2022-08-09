# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time complexity - O(N) because of recursive call, S - O(N) -->Stack
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            # recursively find the longest path in
            # both left child and right child
            left = dfs(root.left)
            right = dfs(root.right)
            
            # update the diameter if left_path plus right_path is larger
            res = max(res, left + right)
            
            # return the longest one between left_path and right_path;
            # remember to add 1 for the path connecting the node and its parent
            return 1 + max(left, right)

        dfs(root)
        return res
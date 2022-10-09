# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        map = {}
		# 1. Add all values to map with remain to k value
		# example: if k is 9 and we found 3 we add [3: 6] to the map
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            else:
                map[root.val] = k - root.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
		# 2. Loop keys in map and check if pair is the one of keys in the map
		# If key is the same with pair we continue to the next loop 
		# Because It wouldn't have the same value in BST
        for k in map:
            pair = map[k]
            if pair == k: continue
            elif pair in map: return True
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, val) :
            if node.val == val :
                return True
            if node.left and dfs(node.left, path, val) : 
                # this indicates that I found the node on the left branch
                #If it is True you can append L and no need to go 
                #to the right side of the tree 
                path.append('L')
            elif node.right and dfs(node.right, path, val) :
                path.append('R')
            return len(path) > 0 # failed to find a path
        
        start, dest = [], []
        dfs(root, start, startValue) # create a start node path
        dfs(root, dest, destValue) # create a dest node path
        
        while start and dest and start[-1] == dest[-1] :
            #Popping because both the nodes have followed the same path for eg 
            #in the following tree if the path is 1 -- > 2 then we need to remove 5 as both               # have followed the same path 
            #             5
            #            / \
            #           2   4
            #          /\
            #         1  3
            start.pop()
            dest.pop()
        
        return 'U'*len(start) + ''.join(reversed(dest))
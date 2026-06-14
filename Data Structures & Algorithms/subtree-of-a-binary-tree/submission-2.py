# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# traverse until you find the same node
# based on subroot, follow on main tree to see if it is same
#   if it is same return true
#   if there is a difference, continue iterating through the tree
#   unsure if there is case of more than 1 of same node located in tree, current imp assumes no


# base case includes nothing and 1 other node
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None: return True
        if root is None or subRoot is None: return False

        if root and subRoot and root.val == subRoot.val:
            if self.checkTree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        if root and subRoot and root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return False
    
    def checkTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None: return True
        if root is None or subRoot is None: return False

        if root and subRoot and root.val == subRoot.val:
            return self.checkTree(root.left, subRoot.left) and self.checkTree(root.right, subRoot.right)
        else: return False









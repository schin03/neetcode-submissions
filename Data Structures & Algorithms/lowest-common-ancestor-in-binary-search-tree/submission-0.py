# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# bc its bst, smt to do with vals being greater/less than curr node
#   if p and q split at a node, then we know thats the youngest ansestor

#   if both go to 1 side, we can just go there instead of checking the side

#   if curr node = p or q, and alt is child, then ret curr val

# would answer be recursive? prob
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        
        smaller = p if p.val < q.val else q
        larger = p if p.val > q.val else q

        # split case
        if root.val >= smaller.val and root.val <= larger.val: return root

        # root is either node and other is descendant
        if root == smaller or root == larger: return root

        if root.val > larger.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


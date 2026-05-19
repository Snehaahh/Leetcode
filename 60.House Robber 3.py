class Solution(object):
    def rob(self, root):
        def travel(node):
            if not node:
                return (0,0)
            leftval = travel(node.left) 
            rightval = travel(node.right)
            robbed = node.val + leftval[1] + rightval[1]
            skipped = max(leftval) + max(rightval)
            return (robbed,skipped)
        return max(travel(root))

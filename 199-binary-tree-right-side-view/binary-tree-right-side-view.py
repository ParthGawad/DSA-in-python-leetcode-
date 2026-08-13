# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # solving it using Level Order Traversal (BFS)
        res = []
        q = collections.deque([root])

        # while queue persist
        while q : 
            # initialize rightSide var pointer
            rightSide = None 
            # no of nodes in the current level of the binary tree
            qlen = len(q)

            # iterating through all the nodes in the current level 
            for _ in range(qlen) :
                # pop left element in the queue
                node = q.popleft()
                # If an element exist, then
                if node :
                    # since we are doing left to right strictly,the variable `rightSide` gets overridden every iteration, therefore at the end of the for loop, the end node of that level will override the `rightSide` variable in the end, ensurring we will get the right-most node or the end visible node in that level 
                    rightSide = node 
                    # append the left childern of the next level
                    q.append(node.left)
                    # append the right childern of the next level
                    q.append(node.right)
            # if rightside node exist, then append it to the result
            if rightSide :
                res.append(rightSide.val)
        return res
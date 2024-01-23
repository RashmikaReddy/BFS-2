#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# in the zig zag level order traversal, remove the flag of left_to_right and always insert from right to left using the appendleft() for the queue of values. And from queue for each level, take the first element using popleft and append it to final result and return
"""
Approach 1 - Using BFS, can do two approaches
1. Do normal BFS, here inside the level use a deque and appendleft() operation, which helps
the elements stored in the level's q in the reverse order from [3,2] or [4,5]. Then after
each level, do the popleft() to get the first element and append it to a result list. 
2. In the BFS, first insert the right child and then left child into the queue, which would make the traversal like [3,2], no need to use appendleft here. Then for each level, do popleft on the level's queue to get the first element and return the result
TC - O(N), SC - O(N/2) ~ O(N). Here the SC is the diameter of the tree, in worst case is N/2 for a complete binary tree
Approach 2 - Using DFS, iterate the right child and then the left child, and if the level_order does not have an entry for this height yet, then make an entry. As we are recursing right and left, whatever is the first element we are storing it only.
TC - O(N), SC - O(H) - H - height of the tree - logN
"""
from typing import List, Optional
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        final_result = []
        q = deque()
        val_q = deque()
        q.append(root)
        while q:
            size = len(q)
            while size:
                node = q.popleft()
                if node:
                    val_q.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                size -= 1
            final_result.append(val_q.popleft())
            val_q = deque()
        return final_result

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_order = []
        def dfs(root, height):
            if not root:
                return
            #If the level_order does not have an entry for this height yet, then make an entry. As we are recursing right and left, whatever is the first element we are storing it only.
            if len(level_order) == height:
                level_order.append(root.val)
            dfs(root.right, height+1)
            dfs(root.left, height+1)
        dfs(root, 0)
        return level_order
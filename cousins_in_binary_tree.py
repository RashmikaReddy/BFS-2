# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Approach 1:
1. Use BFS, use two bool variables x_flag, y_flag, if for a node popped from q, if the children of the popped_node are x and y, 
then they are siblings but not cousins so return false, and if after a level, x is found and y is found and because they 
are not siblings(did not return false), they are cousins, so return true. Otherwise retrun False
TC - O(N), SC - O(N)
2. Use DFS, iterate the tree, get the depth of the x, y, parents of x, y and then compare in the end, 
if depth_x == depth_y and parent_x not equal to parent_y then return true else False
TC - O(N), SC -O(H)
"""
from collections import deque
from typing import Optional, List
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        if not root:
            return False
        q.append(root)
        while q:
            size = len(q)
            x_flag, y_flag = False, False

            while size:
                pop_node = q.popleft()
                if pop_node:
                    if pop_node.left and pop_node.right:
                        left_val = pop_node.left.val
                        right_val = pop_node.right.val
                        if (left_val == x and right_val == y) or (left_val == y and right_val == x):
                            return False
                    if pop_node.left:
                        if pop_node.left.val == x:
                            x_flag = True
                        elif pop_node.left.val == y:
                            y_flag = True
                        q.append(pop_node.left)    
                    if pop_node.right:
                        if pop_node.right.val == x:
                            x_flag = True
                        elif pop_node.right.val == y:
                            y_flag = True
                        q.append(pop_node.right)
                size -= 1
            if x_flag and y_flag:
                return True
            if x_flag or y_flag:
                return False
        return False
        
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth_x, depth_y = 0, 0
        parent_x, parent_y = None, None
        def dfs(root, depth, parent):
            nonlocal depth_x, depth_y, parent_x, parent_y
            if not root:
                return
            if root.val == x:
                depth_x = depth
                parent_x = parent
            if root.val == y:
                depth_y = depth
                parent_y = parent
            dfs(root.left, depth+1, root)
            dfs(root.right, depth+1, root)
        
        dfs(root, 0, None)
        if depth_x == depth_y and parent_x != parent_y:
            return True
        return False


                
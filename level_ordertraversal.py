from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        result.append(current.val)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return result

# Example Usage:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(level_order_traversal(root))  # Output: [1, 2, 3, 4, 5]

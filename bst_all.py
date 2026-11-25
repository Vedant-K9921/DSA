from collections import deque


# 1. Define a single Node in the tree
class Node:

  def __init__(self, value):
    self.value = value
    self.left = None  # Points to smaller values
    self.right = None  # Points to larger values


# 2. Define the Binary Search Tree class
class BinarySearchTree:

  def __init__(self):
    self.root = None  # The tree starts out empty

  # --- INSERTION ---
  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
    else:
      self._insert_recursive(self.root, value)

  def _insert_recursive(self, current_node, value):
    if value < current_node.value:
      if current_node.left is None:
        current_node.left = Node(value)
      else:
        self._insert_recursive(current_node.left, value)
    elif value > current_node.value:
      if current_node.right is None:
        current_node.right = Node(value)
      else:
        self._insert_recursive(current_node.right, value)
    # Note: Duplicate values are ignored in standard BSTs

  # --- SEARCH ---
  def search(self, value):
    return self._search_recursive(self.root, value)

  def _search_recursive(self, current_node, value):
    if current_node is None:
      return False
    if value == current_node.value:
      return True
    elif value < current_node.value:
      return self._search_recursive(current_node.left, value)
    else:
      return self._search_recursive(current_node.right, value)

  # --- MIN & MAX VALUES ---
  def find_min(self):
    if self.root is None:
      return None
    current = self.root
    while current.left is not None:  # Keep going left for the smallest value
      current = current.left
    return current.value

  def find_max(self):
    if self.root is None:
      return None
    current = self.root
    while current.right is not None:  # Keep going right for the largest value
      current = current.right
    return current.value

  # --- DELETION ---
  def delete(self, value):
    self.root = self._delete_recursive(self.root, value)

  def _delete_recursive(self, current_node, value):
    if current_node is None:
      return None

    # Step 1: Find the node to delete
    if value < current_node.value:
      current_node.left = self._delete_recursive(current_node.left, value)
    elif value > current_node.value:
      current_node.right = self._delete_recursive(current_node.right, value)
    else:
      # Step 2: Node found! Handle the 3 deletion cases:

      # Case 1: Node has no children (Leaf node)
      if current_node.left is None and current_node.right is None:
        return None

      # Case 2: Node has only 1 child
      if current_node.left is None:
        return current_node.right
      if current_node.right is None:
        return current_node.left

      # Case 3: Node has 2 children
      # Find the smallest value in the right subtree (in-order successor)
      successor = current_node.right
      while successor.left is not None:
        successor = successor.left

      # Replace current node's value with the successor's value
      current_node.value = successor.value
      # Delete the duplicate successor node from the right subtree
      current_node.right = self._delete_recursive(
          current_node.right, successor.value
      )

    return current_node

  # --- TRAVERSALS (Ways to visit all nodes) ---

  # 1. In-Order (Left -> Root -> Right): Gives values in sorted order
  def inorder(self):
    result = []
    self._inorder_recursive(self.root, result)
    return result

  def _inorder_recursive(self, node, result):
    if node:
      self._inorder_recursive(node.left, result)
      result.append(node.value)
      self._inorder_recursive(node.right, result)

  # 2. Pre-Order (Root -> Left -> Right): Useful for copying a tree
  def preorder(self):
    result = []
    self._preorder_recursive(self.root, result)
    return result

  def _preorder_recursive(self, node, result):
    if node:
      result.append(node.value)
      self._preorder_recursive(node.left, result)
      self._preorder_recursive(node.right, result)

  # 3. Post-Order (Left -> Right -> Root): Useful for deleting a tree
  def postorder(self):
    result = []
    self._postorder_recursive(self.root, result)
    return result

  def _postorder_recursive(self, node, result):
    if node:
      self._postorder_recursive(node.left, result)
      self._postorder_recursive(node.right, result)
      result.append(node.value)

  # 4. Level-Order / BFS (Top to bottom, left to right)
  def level_order(self):
    if self.root is None:
      return []
    result = []
    queue = deque([self.root])

    while queue:
      current = queue.popleft()
      result.append(current.value)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
    return result

  # --- UTILITY FUNCTIONS ---
  def height(self):
    return self._height_recursive(self.root)

  def _height_recursive(self, node):
    if node is None:
      return -1  # Height of an empty tree is -1 (0 for a single root node)
    left_height = self._height_recursive(node.left)
    right_height = self._height_recursive(node.right)
    return 1 + max(left_height, right_height)

  def count_nodes(self):
    return self._count_recursive(self.root)

  def _count_recursive(self, node):
    if node is None:
      return 0
    return (
        1
        + self._count_recursive(node.left)
        + self._count_recursive(node.right)
    )


# ==========================================
# EXAMPLE USAGE (Run this to test the code!)
# ==========================================
if __name__ == "__main__":
  bst = BinarySearchTree()

  # Insert numbers into the tree
  numbers = [50, 30, 70, 20, 40, 60, 80]
  for num in numbers:
    bst.insert(num)

  print("In-Order (Sorted):", bst.inorder())
  print("Pre-Order:        ", bst.preorder())
  print("Post-Order:       ", bst.postorder())
  print("Level-Order:      ", bst.level_order())

  print("\nSearch for 40:", bst.search(40))  # True
  print("Search for 99:", bst.search(99))  # False

  print("\nMinimum value:", bst.find_min())  # 20
  print("Maximum value:", bst.find_max())  # 80
  print("Tree height:  ", bst.height())  # 2
  print("Total nodes:  ", bst.count_nodes())  # 7

  # Delete a node with two children (50)
  bst.delete(50)
  print("\nIn-Order after deleting 50:", bst.inorder())

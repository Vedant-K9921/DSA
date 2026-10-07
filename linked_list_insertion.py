from node import Node
from linked_list_base import SinglyLinkedList

class InsertionLinkedList(SinglyLinkedList):
    """Extends basic list with insertion operations."""
    
    def insert_at_beginning(self, data):
        """Inserts a new node at the very start of the list (Prepend)."""
        new_node = Node(data)
        new_node.next = self.head  # Link new node to the current head
        self.head = new_node       # Move head to point to the new node

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list (Append)."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:  # Traverse until the last node
            current = current.next
        current.next = new_node  # Link the last node to the new node

    def insert_at_position(self, position, data):
        """Inserts a node at a specific 0-indexed position."""
        if position < 0:
            print("Invalid position.")
            return
        
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        # Traverse to the node just before the insertion position
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds.")
                return
            current = current.next

        if current is None:
            print("Position out of bounds.")
            return

        new_node.next = current.next  # Point new node to the next target
        current.next = new_node       # Point current node to the new node

from node import Node

class SinglyLinkedList:
    """Manages singly linked list initialization and display operations."""
    def __init__(self):
        self.head = None  # Points to the first node

    def display(self):
        """Prints the entire linked list from head to end."""
        if not self.head:
            print("List is empty.")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next  # Move to the next node
        print("None")

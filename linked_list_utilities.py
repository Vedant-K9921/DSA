from linked_list_deletion import DeletionLinkedList

class CompleteLinkedList(DeletionLinkedList):
    """Extends list with utility methods like search, update, and reverse."""
    
    def search(self, key):
        """Checks if a target value exists and returns its 0-indexed position."""
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position  # Key found
            current = current.next
            position += 1
        return -1  # Key not found

    def update(self, position, new_data):
        """Modifies the content of a node at a specific 0-indexed position."""
        current = self.head
        for _ in range(position):
            if current is None:
                print("Position out of bounds.")
                return
            current = current.next
        
        if current is None:
            print("Position out of bounds.")
            return
        current.data = new_data  # Overwrite data

    def reverse(self):
        """Reverses the linked list in place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Temporarily store the next link
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move pointers forward
            current = next_node
        self.head = prev  # Set the last non-null node as the new head

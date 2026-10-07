from linked_list_insertion import InsertionLinkedList

class DeletionLinkedList(InsertionLinkedList):
    """Extends insertion list with deletion operations."""
    
    def delete_from_beginning(self):
        """Removes the first node of the list."""
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        self.head = self.head.next  # Shift the head pointer to the next node

    def delete_from_end(self):
        """Removes the last node of the list."""
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        
        if not self.head.next:  # Only one element exists
            self.head = None
            return

        current = self.head
        # Traverse to the second-to-last node
        while current.next.next:
            current = current.next
        current.next = None  # Disconnect the final node

    def delete_at_position(self, position):
        """Removes a node at a specific 0-indexed position."""
        if not self.head:
            print("List is empty.")
            return
        
        if position == 0:
            self.delete_from_beginning()
            return

        current = self.head
        # Traverse to the node right before the targeted index
        for _ in range(position - 1):
            if current.next is None:
                print("Position out of bounds.")
                return
            current = current.next

        if current.next is None:
            print("Position out of bounds.")
            return

        # Bypass the deleted node by linking to its next reference
        current.next = current.next.next

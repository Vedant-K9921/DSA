class Node:
    """Represents a single node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Stores the actual value
        self.next = None  # Reference pointer to the next node


class SinglyLinkedList:
    """Manages singly linked list operations."""
    def __init__(self):
        self.head = None  # Points to the first node

    # --- 1. TRAVERSAL ---
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

    # --- 2. INSERTION OPERATIONS ---
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

    # --- 3. DELETION OPERATIONS ---
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

    # --- 4. UTILITY METHODS (SEARCH, UPDATE, REVERSE) ---
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


# --- Driver Code to Test All Operations ---
if __name__ == "__main__":
    llist = SinglyLinkedList()

    print("--- Testing Insertions ---")
    llist.insert_at_end(10)
    llist.insert_at_end(20)
    llist.insert_at_beginning(5)
    llist.insert_at_position(2, 15)  # List should be: 5 -> 10 -> 15 -> 20 -> None
    llist.display()

    print("\n--- Testing Search & Update ---")
    print(f"Position of element '15': {llist.search(15)}")
    llist.update(2, 18)  # Update position 2 from 15 to 18
    llist.display()

    print("\n--- Testing Deletions ---")
    llist.delete_from_beginning()  # Removes 5
    llist.delete_from_end()        # Removes 20
    llist.delete_at_position(1)    # Removes 18 (which was at index 1)
    llist.display()                # Output should be: 10 -> None

    print("\n--- Testing Reversal ---")
    # Refilling the list for a clear demo
    llist.insert_at_end(20)
    llist.insert_at_end(30)
    print("Original List:")
    llist.display()
    print("Reversed List:")
    llist.reverse()
    llist.display()

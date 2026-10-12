
# Represents a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data       # Store the value in the node
        self.next = None       # Initially, point to no next node


# Manages all singly linked list operations
class SinglyLinkedList:
    def __init__(self):
        self.head = None       # Initially, the list is empty

    # 1. TRAVERSAL: Display all nodes
    def display(self):
        if not self.head:      # Check whether the list is empty
            print("List is empty.")
            return             # Stop the method

        current = self.head    # Start from the first node

        while current:         # Continue until current becomes None
            print(current.data, end=" -> ")  # Print current value
            current = current.next           # Move to the next node

        print("None")          # Mark the end of the list

    # 2. INSERTION: Add a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link it to the current first node
        self.head = new_node   # Make the new node the first node

    # INSERTION: Add a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node

        if not self.head:      # Check whether the list is empty
            self.head = new_node  # Make the new node the first node
            return

        current = self.head    # Start from the first node

        while current.next:    # Find the last node
            current = current.next

        current.next = new_node  # Attach the new node at the end

    # INSERTION: Add a node at a specific 0-based position
    def insert_at_position(self, position, data):
        if position < 0:       # Reject negative positions
            print("Invalid position.")
            return

        if position == 0:      # Position 0 means the beginning
            self.insert_at_beginning(data)
            return

        current = self.head    # Start from the first node

        # Move to the node just before the target position
        for _ in range(position - 1):
            if current is None:  # Check whether position is invalid
                print("Position out of bounds.")
                return
            current = current.next  # Move to the next node

        if current is None:    # Check whether the position is too large
            print("Position out of bounds.")
            return

        new_node = Node(data)  # Create the new node
        new_node.next = current.next  # Link it to the next node
        current.next = new_node       # Link the current node to it

    # 3. DELETION: Remove the first node
    def delete_from_beginning(self):
        if not self.head:      # Check whether the list is empty
            print("List is empty. Nothing to delete.")
            return

        self.head = self.head.next  # Move head to the second node

    # DELETION: Remove the last node
    def delete_from_end(self):
        if not self.head:      # Check whether the list is empty
            print("List is empty. Nothing to delete.")
            return

        if not self.head.next: # Check whether only one node exists
            self.head = None   # Make the list empty
            return

        current = self.head    # Start from the first node

        # Move to the second-last node
        while current.next.next:
            current = current.next

        current.next = None    # Remove the link to the last node

    # DELETION: Remove a node at a specific 0-based position
    def delete_at_position(self, position):
        if position < 0:       # Reject negative positions
            print("Invalid position.")
            return

        if not self.head:      # Check whether the list is empty
            print("List is empty.")
            return

        if position == 0:      # Delete the first node
            self.delete_from_beginning()
            return

        current = self.head    # Start from the first node

        # Move to the node before the target position
        for _ in range(position - 1):
            if current.next is None:  # Check whether position is invalid
                print("Position out of bounds.")
                return
            current = current.next    # Move to the next node

        if current.next is None:  # Target position does not exist
            print("Position out of bounds.")
            return

        # Skip the target node and link to the following node
        current.next = current.next.next

    # 4. SEARCH: Find a value and return its position
    def search(self, key):
        current = self.head    # Start from the first node
        position = 0           # Initialize the index at zero

        while current:         # Traverse the list
            if current.data == key:  # Check whether the value matches
                return position     # Return the matching index

            current = current.next  # Move to the next node
            position += 1           # Increment the index

        return -1              # Return -1 if the value is not found

    # UPDATE: Change the value at a specific position
    def update(self, position, new_data):
        if position < 0:       # Reject negative positions
            print("Invalid position.")
            return

        current = self.head    # Start from the first node

        # Move to the requested position
        for _ in range(position):
            if current is None:  # Check whether position is invalid
                print("Position out of bounds.")
                return
            current = current.next  # Move to the next node

        if current is None:    # Check whether the target exists
            print("Position out of bounds.")
            return

        current.data = new_data  # Replace the old value with the new one

    # REVERSE: Reverse the links between nodes
    def reverse(self):
        prev = None            # Previous node is initially empty
        current = self.head    # Start from the first node

        while current:         # Process each node
            next_node = current.next  # Save the next node
            current.next = prev       # Reverse the current link
            prev = current            # Move prev to the current node
            current = next_node       # Continue to the saved next node

        self.head = prev       # Set the last node as the new head


# 5. DRIVER CODE: Test all linked list operations
if __name__ == "__main__":

    # Create an empty linked list
    llist = SinglyLinkedList()

    # Test insertion operations
    print("--- Testing Insertions ---")
    llist.insert_at_end(10)         # List: 10
    llist.insert_at_end(20)         # List: 10 -> 20
    llist.insert_at_beginning(5)    # List: 5 -> 10 -> 20
    llist.insert_at_position(2, 15) # List: 5 -> 10 -> 15 -> 20
    llist.display()                 # Display the list

    # Test search and update operations
    print("\n--- Testing Search & Update ---")
    print("Position of 15:", llist.search(15))  # Expected: 2
    llist.update(2, 18)             # Change value at index 2 to 18
    llist.display()                 # Display the updated list

    # Test deletion operations
    print("\n--- Testing Deletions ---")
    llist.delete_from_beginning()   # Remove 5
    llist.delete_from_end()         # Remove 20
    llist.delete_at_position(1)     # Remove 18
    llist.display()                 # Expected: 10 -> None

    # Add nodes again to demonstrate reversal
    print("\n--- Testing Reversal ---")
    llist.insert_at_end(20)         # Append 20
    llist.insert_at_end(30)         # Append 30

    print("Original List:")
    llist.display()                 # Expected: 10 -> 20 -> 30 -> None

    # Reverse the list
    llist.reverse()

    print("Reversed List:")
    llist.display()                 # Expected: 30 -> 20 -> 10 -> None

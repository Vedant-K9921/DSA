class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current

    def display(self):
        """Print the list."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements))

    def rev_display(self):
        """Print the list in reverse order."""
        if not self.head:
            return
        last = self.head
        while last.next:
            last = last.next
        while last:
            print(last.data, end=" ")
            last = last.prev
        print() # Newline for clean output

    def insert(self, index, data):
        """Insert a node at a specific index (0-based)."""
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        new_node = Node(data)

        # Case 1: Insert at the beginning (index 0)
        if index == 0:
            if self.head:
                self.head.prev = new_node
                new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_index = 0
        while current and current_index < index - 1:
            current = current.next
            current_index += 1

        if not current:
            raise IndexError("Index out of bounds")

        # Case 2: Insert in the middle or at the end
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete(self, index):
        """Delete a node at a specific index (0-based)."""
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        if not self.head:
            raise IndexError("Delete from empty list")

        current = self.head

        # Case 1: Deleting the head node (index 0)
        if index == 0:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        # Traverse to the target index
        current_index = 0
        while current and current_index < index:
            current = current.next
            current_index += 1

        # If index does not exist
        if not current:
            raise IndexError("Index out of bounds")

        # Case 2: Deleting from the middle or the end
        if current.next: # If it's a middle node
            current.next.prev = current.prev
        
        if current.prev: # If it's a middle or tail node
            current.prev.next = current.next

    def occurence(self,index):
        count=0
        temp=self.head
        while temp:
            if index==temp.data:
                count+=1
            temp=temp.next
        print("Occurence : ",count)


# --- Example Usage ---
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(40)
dll.append(40)
dll.append(30)

dll.occurence(40)

print("Original List:")
dll.display() # Output: 10 <-> 20 <-> 30 <-> 40

print("\nDeleting head (index 0):")
dll.delete(0)
dll.display() # Output: 20 <-> 30 <-> 40

print("\nDeleting middle node (index 1):")
dll.delete(1)
dll.display() # Output: 20 <-> 40

print("\nDeleting tail node (index 1):")
dll.delete(1)
dll.display() # Output: 20

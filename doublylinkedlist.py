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

        # Find the last node
        current = self.head
        while current.next:
            current = current.next

        # Link the new node
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
        last=self.head
        while(last.next!=None):
            last=last.next
        while last:
            print(last.data,end=" ")
            last=last.prev

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

        # Traverse to the node just before the target index
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

# --- Example Usage ---
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

dll.display()
dll.rev_display()
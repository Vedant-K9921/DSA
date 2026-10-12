
# Define a node of the linked list
class Node:
    def __init__(self, val):
        self.data = val       # Store the node's value
        self.next = None      # Point to the next node


# Define the linked list
class LinkedList:
    def __init__(self):
        self.head = None      # Initially, the list is empty

    # Add a node at the end of the list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node   # Make the new node the first node
        else:
            temp = self.head       # Start from the first node

            while temp.next:       # Move until the last node
                temp = temp.next

            temp.next = new_node  # Link the last node to the new node

    # Print all node values
    def print(self):
        temp = self.head           # Start from the first node

        while temp:                # Continue until the end
            print(temp.data, end=" ")  # Print the current value
            temp = temp.next       # Move to the next node

        print()                    # Move to the next line

    # Reverse the linked list
    def rev(self):
        curr = self.head           # Start from the first node
        prev = None                # Initially, there is no previous node

        while curr:                # Continue until all nodes are processed
            nextnode = curr.next   # Save the next node
            curr.next = prev       # Reverse the current link
            prev = curr            # Move prev to the current node
            curr = nextnode        # Move curr to the next node

        self.head = prev           # Set the new head to the former last node


# Create an empty linked list
ll = LinkedList()

# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(-30)

# Append nodes to the list
ll.append(n1)
ll.append(n2)
ll.append(n3)

# Print the original linked list
ll.print()     # Output: 10 20 -30

# Reverse the linked list
ll.rev()

# Print the reversed linked list
ll.print()     # Output: -30 20 10

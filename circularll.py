class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def search(self, key):
        if self.head is None:
            return False

        current = self.head

        while True:
            if current.data == key:
                return True

            current = current.next

            if current == self.head:
                return False

    def delete(self, key):
        if self.head is None:
            return False

        current = self.head
        previous = None

        while True:
            if current.data == key:
                # Only one node exists
                if current.next == current:
                    self.head = None

                # Deleting the head
                elif current == self.head:
                    last = self.head

                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head

                # Deleting another node
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

            if current == self.head:
                return False
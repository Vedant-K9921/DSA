class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    # Add Patient
    def add_patient(self, pid, name, priority):
        new_node = Node(pid, name, priority)

        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully!")

    # Display Next Patient
    def display_next(self):
        if self.front is None:
            print("No patients waiting.")
        else:
            print("\nNext Patient:")
            print("ID:", self.front.pid)
            print("Name:", self.front.name)
            print("Priority:", self.front.priority)

    # Remove Patient
    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front
            print("Patient treated:", temp.name)
            self.front = self.front.next

    # Display All Patients
    def display_all(self):
        if self.front is None:
            print("No patients waiting.")
        else:
            temp = self.front
            print("\nWaiting Patients:")

            while temp is not None:
                print("ID:", temp.pid,
                      "| Name:", temp.name,
                      "| Priority:", temp.priority)
                temp = temp.next


# Main Program
pq = PriorityQueue()

while True:
    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority >= 1 and priority <= 3:
            pq.add_patient(pid, name, priority)
        else:
            print("Invalid priority!")

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        print("Exit..............")
        break

    else:
        print("Invalid choice!")
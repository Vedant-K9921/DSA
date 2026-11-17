queue = []
priority_names = {1: "Critical", 2: "Serious", 3: "Normal"}


def enqueue(patient_id, name, priority):
    if priority not in [1, 2, 3]:
        print("Invalid priority! Enter 1, 2, or 3.")
        return
    queue.append((priority, patient_id, name))
    print(f"Added: {name} (ID: {patient_id}) - {priority_names[priority]}")


def display_next():
    if not queue:
        print("No patients waiting.")
        return
    sorted_queue = sorted(queue, key=lambda x: x[0])
    priority, patient_id, name = sorted_queue[0]
    print(f"\nNext Patient -> ID: {patient_id} | Name: {name} | Condition: {priority_names[priority]}")


def dequeue():
    if not queue:
        print("No patients to treat.")
        return
    queue.sort(key=lambda x: x[0])
    priority, patient_id, name = queue.pop(0)
    print(f"\nTreated & Removed -> ID: {patient_id} | Name: {name} ({priority_names[priority]})")


def display_all():
    if not queue:
        print("\nWaiting list is empty.")
        return
    print("\n--- All Waiting Patients ---")
    for priority, patient_id, name in sorted(queue, key=lambda x: x[0]):
        print(f"ID: {patient_id} | Name: {name} | Priority: {priority} ({priority_names[priority]})")
    print("----------------------------")


while True:
    print("\n=== Hospital Emergency System ===")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Treat Next Patient (Remove)")
    print("4. Display All Waiting Patients")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        p_id = input("Enter Patient ID: ")
        p_name = input("Enter Patient Name: ")
        p_prio = int(input("Enter Priority (1=Critical, 2=Serious, 3=Normal): "))
        enqueue(p_id, p_name, p_prio)

    elif choice == '2':
        display_next()

    elif choice == '3':
        dequeue()

    elif choice == '4':
        display_all()

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
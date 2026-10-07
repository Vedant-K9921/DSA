from linked_list_utilities import CompleteLinkedList

if __name__ == "__main__":
    llist = CompleteLinkedList()

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
    llist.insert_at_end(20)
    llist.insert_at_end(30)
    print("Original List:")
    llist.display()
    print("Reversed List:")
    llist.reverse()
    llist.display()

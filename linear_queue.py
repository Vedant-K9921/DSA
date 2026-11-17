class Queue:
    def __init__(self):
        self.queue = []

    # 1. Enqueue an element into the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # 2. Dequeue an element from the queue
    def dequeue(self):
        if not self.queue:
            print("Queue is empty! (Underflow)")
            return None
        return self.queue.pop(0)

    # 3. Display the queue
    def display(self):
        print("Queue (Front to Rear):", self.queue)

    # 4. Reverse the queue using a stack
    def reverse_queue(self):
        stack = []
        # Move all elements from queue to stack
        while self.queue:
            stack.append(self.queue.pop(0))
        # Move them back to queue (stack LIFO order reverses them)
        while stack:
            self.queue.append(stack.pop())
        print("Queue reversed using stack!")

    # 5. Merge two queues into one
    @staticmethod
    def merge_queues(q1, q2):
        merged_queue = Queue()
        # Combine elements of both queues
        merged_queue.queue = q1.queue.copy() + q2.queue.copy()
        return merged_queue

    # 6. Check if two queues are identical
    @staticmethod
    def are_identical(q1, q2):
        return q1.queue == q2.queue



if __name__ == "__main__":
    print("--- 1, 2 & 3. Enqueue, Dequeue, and Display ---")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    
    print("Dequeued element:", q.dequeue())
    q.display()

    print("\n--- 4. Reverse Queue using Stack ---")
    q.reverse_queue()
    q.display()

    print("\n--- 5. Merge Two Queues ---")
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    
    q2 = Queue()
    q2.enqueue(3)
    q2.enqueue(4)
    
    q3 = Queue.merge_queues(q1, q2)
    print("Merged Queue:")
    q3.display()

    print("\n--- 6. Check if Two Queues are Identical ---")
    qa = Queue()
    qa.enqueue(100)
    qa.enqueue(200)

    qb = Queue()
    qb.enqueue(100)
    qb.enqueue(200)

    qc = Queue()
    qc.enqueue(500)

    print("Are qa and qb identical?", Queue.are_identical(qa, qb))
    print("Are qa and qc identical?", Queue.are_identical(qa, qc))
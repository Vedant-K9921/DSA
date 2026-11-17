class Stack:
    def __init__(self):
        self.stack = []

    # 1. Push operation
    def push(self, item):
        self.stack.append(item)

    # 2. Pop operation
    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    # 3. Display operation
    def display(self):
        print("Current Stack:", self.stack)

    # 4. Reverse a String using a Stack
    def reverse_string(self, text):
        temp_stack = []
        for char in text:
            temp_stack.append(char)
        
        reversed_text = ""
        while temp_stack:
            reversed_text += temp_stack.pop()
        return reversed_text

    # 5. Reverse Stack using another Stack
    def reverse_stack(self):
        aux_stack = []
        while self.stack:
            aux_stack.append(self.stack.pop())
        self.stack = aux_stack


# --- Example Usage ---
s = Stack()

print("--- 1, 2 & 3. Push, Pop, Display ---")
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Popped item:", s.pop())
s.display()

print("\n--- 4. Reverse String ---")
print("Reversed 'python':", s.reverse_string("python"))

print("\n--- 5. Reverse Stack using Another Stack ---")
s.stack = [1, 2, 3, 4, 5]
print("Before reversal:", s.stack)
s.reverse_stack()
print("After reversal:", s.stack)
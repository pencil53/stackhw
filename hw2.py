class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def printStack(self):
        print("Stack:", self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.printStack()
print(f"Top element is {stack.peek()}")
print(f"Stack size is {stack.size()}")
print(f"{stack.pop()} popped from stack")
stack.printStack()

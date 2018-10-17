class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)
    
        
        
def palindrome(word):
    s=Stack()
    for i in word:
        s.push(i)
    w=""
    while not s.isEmpty():
            w=w+s.pop()

    if(w==word):
        print("Palindrome")

    else:
        print("Not a Palindrome")
print(palindrome("abac"))


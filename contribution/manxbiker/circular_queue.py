class Queue(): 
    SIZE = 5 
    def __init__(self): 
        self.__items =[""]*self.SIZE 
        self.__front = -1 
        self.__rear = -1 
 
    def isFull(self): 
        if(self.__front == 0 and self.__rear == self.SIZE -1): 
            return True 
        if(self.__front == self.__rear + 1): 
            return True 
        return False 
 
    def isEmpty(self): 
        if(self.__front == -1): 
            return True        
        return False 
 
    def enQueue(self, element): 
        if(self.isFull()): 
            print("Queue is full") 
        else: 
            if(self.__front == -1): 
                self.__front = 0 
            self.__rear = (self.__rear + 1)%self.SIZE 
            self.__items[self.__rear] = element 
            print("Inserted", element) 
 
    def deQueue(self): 
        if(self.isEmpty()): 
           print("Queue is empty") 
           return -1 
        else: 
            element = self.__items[self.__front] 
            if(self.__front == self.__rear): 
                self.__front = -1 
                self.__rear = -1 
            else: 
                self.__front = (self.__front+1)%self.SIZE 
            return element 
 
    def Display(self): 
        if(self.isEmpty()): 
            print("Empty Queue") 
        else: 
            print("Front",self.__front) 
            print("End", self.__rear) 
            print("Items") 
            i = self.__front 
            while(i != self.__rear): 
                print(self.__items[i]) 
                i = (i+1)%self.SIZE 
            print(self.__items[i]) 
 
myQ = Queue() 
myQ.deQueue() #Should give -1 error 
 
myQ.enQueue(1) 
myQ.enQueue(2) 
myQ.enQueue(3) 
myQ.enQueue(4) 
myQ.enQueue(5) 
 
#This one should fail, queue full
myQ.enQueue(6) 
 
myQ.Display() 
 
x = myQ.deQueue() 
x = myQ.deQueue() 
 
myQ.Display() 

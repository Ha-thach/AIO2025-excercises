class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []
    
    def is_empty(self):
        return self.__queue == [] 
    
    def is_full(self):
        return len(self.__queue) == self.__capacity 
    
    def dequeue(self):
        return self.__queue.pop(0)
    
    def enqueue(self, value):
        self.__queue.append(value)
    
    def front(self):
        return self.__queue[0]

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)


print(queue1.is_full())
queue1.enqueue(2)
print(queue1.front())

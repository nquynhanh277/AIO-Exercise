class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def is_empty(self):
        return len(self.__queue) == 0

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Overflow")
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.__queue.pop[0]

    def front(self):
        if self.is_empty():
            raise Exception("Underflow")
        self.__queue[0]


if __name__ == "__main__":
    queue1 = MyQueue(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.is_full())

    queue2 = MyQueue(capacity=5)
    queue2.enqueue(1)
    assert queue2.is_full() == False
    queue2.enqueue(2)
    print(queue2.front())

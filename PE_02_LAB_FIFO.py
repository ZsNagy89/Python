class QueueError(Exception):  # Choose base class for the new exception.
    def __init__(self):
        Exception.__init__(self)

class Queue:
    def __init__(self):
        self.__stack_list = []

    def put(self, elem):
        self.__stack_list.append(elem)

    def get(self):
        elem=self.__stack_list[0]
        del self.__stack_list[0]
        return elem

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

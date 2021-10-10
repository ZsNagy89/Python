class QueueError(Exception):
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

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self._Queue__stack_list)==0:
            return True
        else:
            return False
    #
    # Write new code here.
    #


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

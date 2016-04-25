vals= [1,20,-4,8,1,9,30]

class MinStack:
    def __init__(self):
        self._stack = []
        self._minRec = []


    def push(self,data):
        self._stack.append(data)
        if not self._minRec or data<=self._minRec[-1]:
            self._minRec.append(data)


    def pop(self):
        if not self._stack:
            return 0
        d = self._stack.pop()
        if d == self._minRec[-1]:
            self._minRec.pop()
        return d

    def get_min(self):
        if not self._minRec:
            return 0
        return self._minRec[-1]

    def is_empty(self):
        if self._stack:
            return False
        return True

minStack = MinStack()
for i in vals:
    minStack.push(i)

while not minStack.is_empty():
    print ("min:", minStack.get_min())
    print ("top:", minStack.pop())
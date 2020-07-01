class MinStack():

    def __init__(self):

        self.a = []

    def push(self, x: int) :
        self.a.append(x)

    def pop(self):
        if self.a is None:
            return
        self.a.pop()

    def top(self):
        return  self.a[-1]

    def getMin(self):
        return  min(self.a)



obj = MinStack()
obj.push(5)
obj.push(1)
obj.push(-2)
obj.push(6)
obj.pop()
print(obj.top())
print(obj.getMin())
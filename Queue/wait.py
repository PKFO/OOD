class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    
inp = list(input("Enter people : "))

Q = Queue(inp)
Q1 = Queue()
Q2 = Queue()
time = 1
time1 = 1
x = 0

while not Q.isEmpty():
    x += 1
    # print(x,"time",str(time))
    # print(x,"time1",str(time1))
    if Q1.size() < 5:
        Q1.enQueue(Q.deQueue())
        print(str(x),Q.items[:],Q1.items[:],Q2.items[:])
    else:
        if Q2.size() <5:
            Q2.enQueue(Q.deQueue())
            print(str(x),Q.items[:],Q1.items[:],Q2.items[:])
    if time1 == 2:
        Q2.deQueue()
        time1 = 0
    if time == 3:
        Q1.deQueue()
        time = 0
    time += 1
    if not Q2.isEmpty():
        time1 += 1
    
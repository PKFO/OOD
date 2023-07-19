class Queue:
    def __init__(self,list = None) :
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
    
def encodemsg(Q1,Q2):
    for c in Q1.items:
        if c == " ":
            pass
        else:
            x = Q2.deQueue()
            if (ord(c) + int(x) <= 90 and ord(c) + int(x) >= 65) or (ord(c) + int(x) >= 97 and ord(c) + int(x) <= 122):
                Q3.enQueue(chr(ord(c) +int(x)))
                Q2.enQueue(x)
            else:
                y = ord(c) - 26
                Q3.enQueue(chr(y + int(x)))
                Q2.enQueue(x)
    return Q3.items

def decodemsg(Q1,Q2):
    for c in Q1.items:
        if c == " ":
            pass
        else:
            x = Q2.deQueue()
            if (ord(c) - int(x) <= 90 and ord(c) - int(x) >= 65) or (ord(c) - int(x) >= 97 and ord(c) - int(x) <= 122):
                Q4.enQueue(chr(ord(c) - int(x)))
                Q2.enQueue(x)
            else:
                y = ord(c) + 26
                Q4.enQueue(chr(y - int(x)))
                Q2.enQueue(x)
    return Q4.items
string,number = (input("Enter String and Code : ").split(","))

Q1 = Queue(list(string))

Q2 = Queue(list(number))

Q3 = Queue()
Q4 = Queue()
print(encodemsg(Q1, Q2))

print(decodemsg(Q1, Q2))

# kquwmSaynpv
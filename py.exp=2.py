import time
start=time.time()
class stack:
    def __init__(self):
        self.items=[]
    def isempty (self):
        return self.item==[]
    def push (self,item):
        self.items.append(item)
        print(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def Size(self,items):
     return len(self.item)
s=Stack
print(s.isempty())
print("push")
s.push(11)
s.push(12)
s.push(13)
print("peek",s.peek())
print("pop")
print(s.pop())
print(s.pop())
print("size",s.size())
end=time.time()
print(f"Runtime of the program is {end-start 3")

    
    

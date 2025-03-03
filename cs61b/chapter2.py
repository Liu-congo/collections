# Textbook 2 pass by value VS. pass by reference
x = 5
y = x
x = 2 
print(x)
print(y)

# Textbook 2 IntList
class IntList:
    def __init__(self, cur:int, rest=None):
        self.cur = cur
        self.rest = rest

    def __repr__(self):
        return f"IntList({self.cur}, {self.rest})"
    
    def size(self):
        if self.rest == None:
            return 1
        else:
            return 1 + self.rest.size()
        
    def iterativeSize(self):
        total_size = 0
        tmp = self
        while tmp != None:
            total_size += 1
            tmp = tmp.rest
        return total_size

    def get(self, n):
        idx = 0
        tmp = self
        while idx != n:
            idx += 1
            try:
                tmp = tmp.rest
            except Exception as e:
                print(e)
                return
        assert tmp != None, "n out of List range"
        return tmp.cur
    
L = IntList(5, None)
L.rest = IntList(10, None)
L.rest.rest = IntList(15, None)
print(L)
print(L.size())
print(L.iterativeSize())
print(L.get(2))

# Lab2
class IntList:
    def __init__(self, cur:int, rest=None):
        self.cur = cur
        self.rest = rest

    def __repr__(self):
        return f"{self.cur} -> {self.rest}"
    
    def size(self):
        if self.rest == None:
            return 1
        else:
            return 1 + self.rest.size()
        
    def iterativeSize(self):
        total_size = 0
        tmp = self
        while tmp != None:
            total_size += 1
            tmp = tmp.rest
        return total_size

    def iterativeGet(self, n):
        idx = 0
        tmp = self
        while idx != n:
            idx += 1
            try:
                tmp = tmp.rest
            except Exception as e:
                print(e)
                return
        assert tmp != None, "n out of List range"
        return tmp.cur
    
    def get(self, n):
        if n == 0:
            return self.cur
        else:
            return self.rest.get(n - 1)
        
    @staticmethod
    def of(*args):
        if len(args) == 0:
            return None
        return IntList(args[0], IntList.of(*args[1:]))
    
    def dSquareList(self):
        self.cur = self.cur * self.cur
        if self.rest == None:
            return
        return self.rest.dSquareList()
    
    def squareListRecursive(self):
        if self.rest == None:
            return IntList(self.cur * self.cur, None)
        return IntList(self.cur * self.cur, self.rest.squareListRecursive())
    
    def squareListIterative(self):
        outputIntList = IntList(self.cur * self.cur, None)
        raw_iter = self
        new_iter = outputIntList
        while raw_iter.rest != None:
            raw_iter = raw_iter.rest
            new_iter.rest = IntList(raw_iter.cur * raw_iter.cur, None)
            new_iter = new_iter.rest
        return outputIntList
    
    @staticmethod
    def dcatenate(A: IntList, B: IntList):
        tmp = A
        while tmp.rest != None:
            tmp = tmp.rest
        tmp.rest = B
        return
    
    @staticmethod
    def catenate(A: IntList, B: IntList):
        import copy
        outputIntList = copy.deepcopy(A)
        tmp = outputIntList
        while tmp.rest != None:
            tmp = tmp.rest
        tmp.rest = B
        return outputIntList
    

L = IntList.of(1,2,3,4,5)
print(L)
L.dSquareList()
print(L)
L1 = L.squareListRecursive()
print(L1)
print(L)
L2 = L.squareListIterative()
print(L2)
print(L)
IntList.dcatenate(L, L1)
print(L)
L3 = IntList.catenate(L, L1)
print(L)
print(L3)

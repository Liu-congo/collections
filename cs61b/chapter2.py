# Textbook 2 pass by value VS. pass by reference
x = 5
y = x
x = 2 
print(x)
print(y)

# Textbook 2 IntList
# class IntList:
#     def __init__(self, cur:int, rest=None):
#         self.cur = cur
#         self.rest = rest

#     def __repr__(self):
#         return f"IntList({self.cur}, {self.rest})"
    
#     def size(self):
#         if self.rest == None:
#             return 1
#         else:
#             return 1 + self.rest.size()
        
#     def iterativeSize(self):
#         total_size = 0
#         tmp = self
#         while tmp != None:
#             total_size += 1
#             tmp = tmp.rest
#         return total_size

#     def get(self, n):
#         idx = 0
#         tmp = self
#         while idx != n:
#             idx += 1
#             try:
#                 tmp = tmp.rest
#             except Exception as e:
#                 print(e)
#                 return
#         assert tmp != None, "n out of List range"
#         return tmp.cur
    
# L = IntList(5, None)
# L.rest = IntList(10, None)
# L.rest.rest = IntList(15, None)
# print(L)
# print(L.size())
# print(L.iterativeSize())
# print(L.get(2))

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
    def dcatenate(A, B):
        tmp = A
        while tmp.rest != None:
            tmp = tmp.rest
        tmp.rest = B
        return
    
    @staticmethod
    def catenate(A, B):
        import copy
        outputIntList = copy.deepcopy(A)
        tmp = outputIntList
        while tmp.rest != None:
            tmp = tmp.rest
        tmp.rest = B
        return outputIntList
    
    def addFirst(self, x:int):
        import copy
        tmp = copy.deepcopy(self)
        self.cur = x
        self.rest = tmp
        return 

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
L = IntList.of(1,2,3,4,5)
L.addFirst(10086)
print(L)

# SLLists
class SLList:
    __slots__ = ['__first', '__size']

    class __IntNode:
        def __init__(self, i:int, n):
            self.item = i
            self.next = n
        
        def __repr__(self):
            if self.next == None:
                return f"{self.item}"
            return f"{self.item}, {self.next}"
        
        def size(self):
            if self.next == None:
                return 1
            else:
                return 1 + self.next.size()
        
    def __init__(self):
        self.__first = None
        self.__size = 0

    def addFirst(self, x:int):
        self.__first = self.__IntNode(x, self.__first)
        self.__size += 1

    def getFirst(self):
        return self.__first.item

    def addLast(self, x:int):
        tmp = SLList()
        if self.__first == None:
            self.__first = self.__IntNode(x, None)
        tmp.__first = self.__first.next
        if tmp.__first == None:
            tmp.__first = self.__IntNode(x, None)
        else:
            tmp.addLast(x)

        self.__first.next = tmp.__first
        self.__size += 1

    
    def size(self):
        return self.__size
    
    def __repr__(self):
        return f"[{self.__first}]"
    

L2 = SLList()
L2.addFirst(10)
L2.addFirst(5)
L2.addFirst(5)
L2.addFirst(5)
L2.addFirst(5)
print(L2.size())
x = L2.getFirst()
print(x)
print(L2)
L2 = SLList()
L2.addLast(10086)
L2.addLast(10086)
L2.addLast(10086)
L2.addLast(10086)
L2.addLast(10086)
print(L2)
print(L2.size())
        
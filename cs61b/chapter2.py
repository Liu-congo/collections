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
    __slots__ = ['__first', '__size','__last']

    class __IntNode:
        def __init__(self, i:int, n):
            self.item = i
            self.next = n
        
        def __repr__(self):
            if self.next == None:
                return f"{self.item}"
            return f"{self.item}, {self.next}"
        
    def __init__(self):
        self.__first = self.__IntNode(None, None)
        self.__last = self.__first
        self.__size = 0

    def addFirst(self, x:int):
        self.__first.next = self.__IntNode(x, self.__first.next)
        self.__size += 1

    def getFirst(self):
        return self.__first.next.item

    # def addLastRecursive(self, x:int):
    #     tmp = SLList()
    #     if self.__first == None:
    #         self.__first = self.__IntNode(x, None)
    #     tmp.__first = self.__first.next
    #     if tmp.__first == None:
    #         tmp.__first = self.__IntNode(x, None)
    #     else:
    #         tmp.addLast(x)

    #     self.__first.next = tmp.__first
    #     self.__size += 1

    # TODO fix the addLast, reference pass / value pass
    def addLast(self, x:int):
        if self.__first.next == None:
            self.__first.next = self.__IntNode(x, None)
            self.__size += 1
            return
        tmp = self.__first
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = self.__IntNode(x, None)
        # self.__last.next = self.__IntNode(x, self.__last.next)
        # self.__last = self.__last.next
        self.__size += 1

    
    def size(self):
        return self.__size
    
    def __repr__(self):
        return f"[{self.__first.next}]"
    

L2 = SLList()
L2.addFirst(10)
L2.addFirst(5)
L2.addLast(10086)
L2.addFirst(5)
L2.addFirst(5)
L2.addFirst(5)
x = L2.getFirst()
print(x)
print(L2)
L2 = SLList()
L2.addLast(10086)
L2.addLast(10086)
L2.addLast(1)
print(L2)
print(L2.size())

class DLList:
    class __IntNode:
        def __init__(self, i, prev=None, next=None):
            self.item = i
            self.prev = prev
            self.next = next
        
        def __repr__(self):
            return f"({self.item})" 
    
    def __init__(self):
        self.__sentinel = self.__IntNode(0) 
        self.__sentinel.prev = self.__sentinel
        self.__sentinel.next = self.__sentinel
        self.__size = 0
    
    def addFirst(self, x):
        new_node = self.__IntNode(x, self.__sentinel, self.__sentinel.next)
        self.__sentinel.next.prev = new_node
        self.__sentinel.next = new_node
        self.__size += 1

    def addLast(self, x):
        new_node = self.__IntNode(x, self.__sentinel.prev, self.__sentinel)
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node
        self.__size += 1
    
    def isEmpty(self) -> bool:
        return True if self.__sentinel.next == self.__sentinel else False

    def size(self) -> int:
        return self.__size

    def removeFirst(self):
        if self.isEmpty():
            return None
        remove_node = self.__sentinel.next
        self.__sentinel.next.next.prev = self.__sentinel
        self.__sentinel.next = self.__sentinel.next.next
        self.__size -= 1
        return remove_node.item

    def removeLast(self):
        if self.isEmpty():
            return None
        remove_node = self.__sentinel.prev
        self.__sentinel.prev.prev.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel.prev.prev
        self.__size -= 1
        return remove_node.item
    
    def get(self, n:int):
        if n < -self.__size or n > self.__size - 1:
            raise IndexError("DLList index out of range")
        cnt = 0
        if n >= 0:
            tmp = self.__sentinel.next
            while cnt != n:
                tmp = tmp.next
                cnt += 1
            return tmp.item
        else:
            tmp = self.__sentinel
            while cnt != n:
                tmp = tmp.prev
                cnt -= 1
            return tmp.item

    def getRecursive(self, n:int):
        # only support situation that index >= 0
        if n < -self.__size or n > self.__size - 1:
            raise IndexError("DLList index out of range")
        if n == 0:
            return self.__sentinel.next.item
        if n == -1:
            return self.__sentinel.prev.item
        elif n > 0:
            tmp = self.removeFirst()
            out = self.getRecursive(n-1)
            self.addFirst(tmp)
            return out
        else:
            tmp = self.removeLast()
            out = self.getRecursive(n+1)
            self.addLast(tmp)
            return out

    @staticmethod
    def copy(dllist=None):
        new_dllist = DLList()
        for i in range(dllist.size()):
            new_dllist.addLast(dllist.get(i))
        return new_dllist
    
    def __repr__(self):
        elements = []
        current = self.__sentinel.next
        while current != self.__sentinel:
            elements.append(str(current.item))
            current = current.next
        return f"[{', '.join(elements)}]"
    
A = DLList()
A.addFirst(1)
A.addFirst(2)
A.addLast(9)
print(A)
k = A.removeFirst()
print(A, k)
k = A.removeLast()
print(A, k)
A.addFirst(2)
A.addLast(9)
A.addFirst(2)
A.addLast(9)
print(A, A.get(0), A.get(3), A.get(4))
B = DLList.copy(A)
A.addLast(10086)
k = A.getRecursive(-6)
print(A, B, k)
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

    def get(self, idx: int):
        if self.__size < 1:
            return None
        if idx > self.__size - 1:
            raise IndexError('Index out of range')
        tmp = self.__first.next
        while idx > 0:
            tmp = tmp.next
            idx -= 1
        return tmp.item
    
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

import array as arr
# Alist only supports integer as it's elements
class AList:
    def __init__(self):
        self.__items = arr.array('i',[0]*128)
        self.__size = 0
        self.usage_ratio = 0.25
        pass

    def addLast(self, x:int):
        if self.__size == self.__items.buffer_info()[1]:
            new_items = arr.array('i',[0]*(self.__size*2))
            new_items[:self.__size] = self.__items[:self.__size]
            self.__items = new_items
        self.__items[self.__size] = x
        self.__size += 1
        return

    def getLast(self) -> int:
        return self.__items[self.__size - 1]

    def get(self, idx: int) -> int:
        return self.__items[idx]

    def size(self) -> int:
        return self.__size

    def removeLast(self) -> int:
        out = self.getLast()
        self.__size -= 1
        if self.__size < self.usage_ratio * self.__items.buffer_info()[1]:
            new_items = arr.array('i',[0]*int(self.__items.buffer_info()[1]/2))
            new_items[:self.__size] = self.__items[:self.__size]
            self.__items = new_items
        return out
    
    def __repr__(self):
        return str(self.__items[:self.__size])
    
A = AList()
print(A.size())
A.addLast(10086)
print(A.getLast())
A.addLast(99)
print(A.getLast(), A.get(0), A.get(1))
A.addLast(36)
print(A.get(2))
k = A.removeLast()
print(A, A.size(), k)
import time
st = time.time()
A = AList()
for i in range(100):
    A.addLast(i)
for i in range(1000):
    A.addLast(A.get(i))
for i in range(900):
    A.removeLast()
print(time.time() - st)
# import time
# st = time.time()
# A = DLList()
# for i in range(10000):
#     A.addLast(i)
# for i in range(10000):
#     A.addLast(A.get(i))
# for i in range(10000):
#     A.removeLast()
# print(time.time() - st)


# Discussion 3 More Practice with Linked List
class SLList:
    class __IntNode:
        def __init__(self, item:int, next=None):
            self.item = item
            self.next = next
        
        def size(self):
            if self.next == None:
                return 1
            else:
                return 1 + self.next.size()

        def __repr__(self):
            return f"{self.item}, {self.next}" if self.next != None else f"{self.item}"
        
    def __init__(self):
        self.__first = self.__IntNode(0, None)

    def addFirst(self, x:int):
        self.__first.next = self.__IntNode(x, self.__first.next)
    
    def insert(self, item:int, position:int):
        tmp = self.__first
        while (position > 0) and (tmp.next != None):
            position -= 1
            tmp = tmp.next
        adding_node = self.__IntNode(item, None)
        if tmp.next == None:
            tmp.next = adding_node
        else:
            adding_node.next = tmp.next
            tmp.next = adding_node
        return
    def reverse(self):
        cursor1 = self.__first.next
        if cursor1.next == None:
            return
        cursor2 = cursor1.next
        cursor1.next = None
        while cursor2 != None:
            tmp = cursor2.next
            cursor2.next = cursor1
            cursor1 = cursor2
            cursor2 = tmp
        self.__first.next = cursor1
        return
    
    def reverseRecursive(self):
        cursor1 = self.__first
        cursor2 = self.__first.next
        while cursor2.next != None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next

        if self.__first.next.size() == 1:
            cursor2.next = None
            return
        else:
            cursor2.next = cursor1
            cursor1.next = None
            self.reverseRecursive()
            self.__first.next = cursor2
        return

    def __repr__(self):
        return f"[{self.__first.next}]"
A = SLList()
A.addFirst(10086)
A.addFirst(310018)
for i in range(5):
    A.insert(i, i+100)
print(A)
A.reverse()
print(A)
A.reverseRecursive()
for i in range(5):
    A.insert(i, i+100)
print(A)

# Discussion3 Arrays
import array as arr
x = arr.array('i',[5,9,14,15])
def insert(cur_array:arr.array, item:int, position:int):
    cur_array_size = cur_array.buffer_info()[1]
    output_array = arr.array('i', [0]*(cur_array_size + 1))
    if position > cur_array_size:
        output_array[:cur_array_size] = cur_array
        output_array[-1] = item
    else:
        output_array[:position] = cur_array[:position]
        output_array[position] = item
        output_array[position+1:] = cur_array[position:]
    return output_array
y = insert(x, 6, 10086)
print(x, y)

def reverse(cur_array:arr.array):
    cur_array_size = cur_array.buffer_info()[1]
    output_array = arr.array('i', [0]*(cur_array_size))
    for i in range(cur_array_size):
        output_array[i] = cur_array[cur_array_size-1-i]
    return output_array
z = reverse(y)
print(z)

def replicate(cur_array:arr.array):
    cur_array_size = cur_array.buffer_info()[1]
    cur_value = cur_array[0]
    extra_e = 0
    for i in range(cur_array_size):
        adding_times = cur_array[i + extra_e] - 1
        for _ in range(adding_times):
            cur_array.insert(i + extra_e + 1, cur_value)
            extra_e += 1
        if i != cur_array_size - 1:
            cur_value = cur_array[i + extra_e + 1]
x = arr.array('i',[3,2,1,2,3])
print(x)
replicate(x)
print(x)
        


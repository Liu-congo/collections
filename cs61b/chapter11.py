# DataIndexedIntegerSet  Naive
class DataIndexedIntegerSet:
    def __init__(self):
        self.__present = [False] * 16

    def insert(self, i: int):
        self.__present[i] = True
    
    def contains(self, i: int):
        return self.__present[i]
tmp = DataIndexedIntegerSet()
tmp.insert(10)
tmp.insert(2)
print(tmp.contains(10), tmp.contains(1))

# DataIndexedWordSet  
class DataIndexedWordSet:
    def __init__(self):
        self.__present = [False] * 10000

    def insert(self, s: str):
        intRep = self.__convertToInt(s)
        self.__present[intRep] = True
    
    def contains(self, s: str):
        intRep = self.__convertToInt(s)
        return self.__present[intRep]

    @staticmethod
    def __convertToInt(s: str):
        intRep = 0
        for i in range(len(s)):
            intRep <<= 5
            intRep += DataIndexedWordSet.__letterNum(s, i)
        return intRep
    
    @staticmethod
    def __letterNum(s: str, i: int):
        ithChar = s[i]
        if ithChar < 'a' or ithChar > 'z':
            raise Exception(f"Illegal Argument '{ithChar}'")
        return ord(ithChar) - ord('a') + 1
    
tmp = DataIndexedWordSet()
tmp.insert("cat")
tmp.insert("dog")
print(tmp.contains("q"),
    #   tmp.contains("369"), 
      tmp.contains("cat"))

from collections import deque
import sys
class LinearProbingHashST:
    def __init__(self, capacity: int = 4):
        self.m = capacity
        self.n = 0
        self.keys = [None] * self.m
        self.vals = [None] * self.m

    def size(self) -> int:
        return self.n
    
    def isEmpty(self) -> bool:
        return self.n == 0
    
    def contains(self, key) -> bool:
        if key:
            return self.get(key) != None
        return Exception("argument to contains() is None")
    
    def __hashTextbook(self, key) -> int:
        return (hash(key) & 0x7fffffff) % self.m
    
    def __hash(self, key) -> int:
        h = hash(key)
        h ^= (h>>20) ^ (h>>12) ^ (h>>7) ^ (h>>4)
        return h & (self.m - 1)
    
    def __resize(self, capacity: int):
        temp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self.keys[i] != None:
                temp.put(self.keys[i], self.vals[i])
        self.keys = temp.keys
        self.vals = temp.vals
        self.m = temp.m

    def put(self, key, val):
        if key == None:
            raise Exception("first argument to put() is None")
        if val == None:
            self.delete(key)
            return
        
        if self.n >= (self.m // 2):
            self.__resize(2 * self.m)
        
        i = self.__hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                self.vals[i] = val
                return
            i = (i + 1)%self.m
        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def get(self, key):
        if key == None:
            raise Exception("argument to get() is None")
        i = self.__hash(key)
        while self.keys[i] != None:
            if self.keys[i] == key:
                return self.vals[i]
            i = (i + 1)%self.m
        return None

    def delete(self, key):
        if key == None:
            raise Exception("argument to delete() is None")
        if not self.contains(key):
            return
        i = self.__hash(key)
        while key != self.keys[i]:
            i = (i + 1) % self.m
        self.keys[i] = None
        self.vals[i] = None
        i = (i + 1)%self.m
        while self.keys[i] != None:
            keyToRehash = self.keys[i]
            valToRehash = self.vals[i]
            self.keys[i] = None
            self.vals[i] = None
            self.n -= 1
            self.put(keyToRehash, valToRehash)
            i = (i + 1) % self.m
        self.n -= 1
        if self.n > 0  and self.n <= self.m / 8:
            self.__resize(self.m // 2)

        assert self.check()

    
    def _keys(self) -> deque:
        q = deque()
        for i in range(self.m):
            if self.keys[i] != None:
                q.append(self.keys[i])
        return q

    def check(self) -> bool:
        if self.m < self.n * 2:
            sys.stderr.write(f"Hash Table size m={self.m}; array size n={self.n}\n")
            return False
        for i in range(self.m):
            if self.keys[i] == None:
                continue
            elif self.get(self.keys[i]) != self.vals[i]:
                sys.stderr.write(f"get [{self.keys[i]}] = {self.get(self.keys[i])}; vals[i] = {self.vals[i]}")
                return False
            else:
                pass
        return True

st = LinearProbingHashST()
i = 0
key = input()
while key != "quit()":
    st.put(key, i)
    i += 1
    key = input()
for s in st._keys():
    print(f"{s}: {st.get(s)}")
    
    





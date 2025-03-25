import array as arr
class ArrayMap:
    def __init__(self):
        self.__keys = arr.array('i', [-1]*128)
        self.__values = arr.array('i', [-1]*128)
        self.__size = 0
    
    def __findKey(self, k: int) -> int:
        try:
            return self.__keys.index(k)
        except:
            return -1

    def put(self, k: int, v: int):
        i = self.__findKey(k)
        if i != -1:
            self.__values[i] = v
            return
        else:
            self.__keys[self.__size] = k
            self.__values[self.__size] = v
            self.__size += 1

    def get(self, k:int) -> int:
        return self.__values[self.__findKey(k)]
    
    def containsKey(self, k: int) -> bool:
        return self.__findKey(k) != -1
    
    def keys(self):
        return self.__keys[:self.__size]
    
ismap = ArrayMap()
ismap.put(1, 3)
print(ismap.get(1))
ismap.put(1, 5)
ismap.put(2, 2)
print(ismap.keys())
print(ismap.containsKey(2))

# simplified version
class BST:
    def __init__(self, label):
        self.__label = label
        self.__left = None
        self.__right = None
        
    def find(self, t, k: int):
        if t == None:
            return None
        if t.__label == k:
            return t
        elif t.__label < k:
            return self.find(t.right, k)
        else:
            return self.find(t.left, k)
        
    def insert(self, t, k:int):
        if t == None:
            return BST(k)
        if k < t.__label:
            t.__left = self.insert(t.__left, k)
        elif k > t.__label:
            t.__right = self.insert(t.__right, k)
        else:
            return t
    
# full version
class BST_full:
    class __Node:
        def __init__(self, key, val, size):
            self.key = key
            self.val = val
            self.size = size
            self.left, self.right = None, None

    def __init__(self):
        self.__root = None

    def isEmpty(self) -> bool:
        return self.size() == 0
    
    def size(self) -> int:
        return self.__size(self.root)

    def __size(self, x: __Node) -> int:
        if x == None:
            return 0
        else:
            return x.size

    def contains(self, key) -> bool:
        if key == None:
            raise Exception("argument to contains is None")
        return self.get(key) != None
    
    def get(self, key):
        return self.__get(self.__root, key)

    def __get(self, x: __Node, key):
        if key == None:
            raise Exception("calls get with a None key")
        if x == None:
            return None
        if key < x.key:
            return self.__get(x.left, key)
        elif key > x.key:
            return self.__get(x.right, key)
        else:
            return x.val
        
    def put(self, key, val):
        if key == None:
            raise Exception("call put with None key")
        if val == None:
            self.delete(key)
            return
        self.__root = self.__put(self.root, key, val)

    def __put(self, x: __Node, key, val):
        if x == None:
            return self.__Node(key, val, 1)
        if key < x.key:
            x.left = self.__put(x.left, key, val)
        elif key > x.key:
            x.right = self.__put(x.right, key, val)
        else:
            x.val = val
        x.size = 1 + self.__size(x.left) + self.__get(x.right)
        return x
    
    def deleteMin(self):
        if self.isEmpty():
            raise Exception("BST underflow")
        self.__root = self.__deleteMin(self.__root)
    
    def __deleteMin(self, x: __Node):
        if x.left == None:
            return x.right
        x.left = self.__deleteMin(x.left)
        x.size = 1 + self.__size(x.left) + self.__get(x.right)
        return x
    
    def deleteMax(self):
        
    
        

        
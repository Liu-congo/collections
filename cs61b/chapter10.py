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


class BST:
    def __init__(self):
        pass

    @staticmethod
    def find(t: BST, k: int):
        if t == None:
            return None
        if 
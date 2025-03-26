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
from queue import Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST_full:
    def __init__(self):
        self.__root = None

    def insert(self, value):
        self.__root = self.__insert_recursive(self.__root, value)
    
    def __insert_recursive(self, node: Node, value):
        if node == None:
            return Node(value)
        if value < node.value:
            node.left = self.__insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self.__insert_recursive(node.right, value)
        else:
            print(f"{value} already exists")
            return node
        return node
    
    def delete(self, value):
        self.__root = self.__delete_recursive(self.__root, value)
    
    def __delete_recursive(self, node: Node, value):
        if node == None:
            return None
        if value < node.value:
            node.left = self.__delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self.__delete_recursive(node.right, value)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                min_node = self.__find_min(node.right)
                node.value = min_node.value
                node.right = self.__delete_recursive(node.right, min_node.value)
        return node
    
    def __find_min(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current
    
    def contains(self, value) -> bool:
        return self.__contains_recursive(self.__root, value)
    
    def __contains_recursive(self, node: Node, value) -> bool:
        if node == None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self.__contains_recursive(node.left, value)
        else:
            return self.__contains_recursive(node.right, value)
        
    def inorder_traversal(self):
        result = []
        self.__inorder_traversal(self.__root, result)
        return result
    
    def __inorder_traversal(self, node: Node, result: list):
        if node:
            self.__inorder_traversal(node.left, result)
            result.append(node.value)
            self.__inorder_traversal(node.right, result)
    
    def level_order_traversal(self):
        result = []
        if not self.__root:
            return result
        queue = Queue()
        queue.put(self.__root)
        while not queue.empty():
            node = queue.get()
            result.append(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        return result
    
    def min_value(self):
        if not self.__root:
            raise Exception("BST is empty")
        current = self.__root
        while current.left:
            current = current.left
        return current.value
    
    def is_empty(self):
        return self.__root == None
    
bst = BST_full()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(1)
bst.insert(4) 
print(bst.level_order_traversal())  
print(bst.inorder_traversal()) 
bst.delete(4)
print(bst.inorder_traversal()) 
bst.delete(5)
print(bst.inorder_traversal()) 
print(bst.contains(3))      
print(bst.contains(10))    
print(bst.min_value())           
print(bst.level_order_traversal())  
        
    
        

        
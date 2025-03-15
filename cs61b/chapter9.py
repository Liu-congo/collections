import time
import random
def testDisjointSets(ds, n):
    print(f"******{ds(0)}******")
    st = time.time()
    test_ds = ds(n)
    print(f"constructor time for {n} nodes:", time.time() - st)
    st = time.time()
    for i in range(n):
        p = random.randint(0, n-1)
        q = random.randint(0, n-1)
        test_ds.connect(p, q)
    print(f"connect time for {n} edges:", time.time() - st)
    st = time.time()
    for i in range(10000):
        p = random.randint(0, n-1)
        q = random.randint(0, n-1)
        test_ds.isConnected(p, q)
    print(f"find time for {n} edges:", time.time() - st)
    print()

class naiveDisjointSets:
    def __init__(self, n:int):
        self.__node_connect_set_dict = {i:set([i])for i in range(n)}
        pass

    def connect(self, p: int, q: int):
        self.__node_connect_set_dict[p].add(q)
        self.__node_connect_set_dict[q].add(p)
        self.__node_connect_set_dict[p].update(self.__node_connect_set_dict[q])
        self.__node_connect_set_dict[q].update(self.__node_connect_set_dict[p])
        return

    def isConnected(self, p: int, q: int) -> bool:
        return (q in self.__node_connect_set_dict[p])

    def __repr__(self):
        return " naiveDisjointSets "

testDisjointSets(naiveDisjointSets, 1000)

class quickFindDisjointSets:
    def __init__(self, n:int):
        self.__node_id = [i for i in range(n)]
        pass

    def connect(self, p: int, q: int):
        p_id, q_id = self.__node_id[p], self.__node_id[q]
        for node_id in self.__node_id:
            node_id = q_id if node_id == p_id else node_id      
        return

    def isConnected(self, p: int, q: int) -> bool:
        return self.__node_id[p] == self.__node_id[q]

    def __repr__(self):
        return " quickFindDisjointSets "

testDisjointSets(quickFindDisjointSets, 1000)

class quickUnionDisjointSets:
    def __init__(self, n:int):
        self.__node_parent = [i for i in range(n)]
        pass

    def __parent(self, p: int) -> int:
        while p != self.__node_parent[p]:
            p = self.__node_parent[p]
        return p

    def connect(self, p: int, q: int):
        p_parent, q_parent = self.__parent(p), self.__parent(q)
        self.__node_parent[p_parent] = q_parent    
        return

    def isConnected(self, p: int, q: int) -> bool:
        return self.__parent(p) == self.__parent(q)

    def __repr__(self):
        return " quickUnionDisjointSets "

testDisjointSets(quickUnionDisjointSets, 1000)

class weightedQuickUnionDisjointSets:
    def __init__(self, n:int):
        self.__node_parent = [i for i in range(n)]
        self.__size = [1] * n
        pass

    def __parent(self, p: int) -> int:
        while p != self.__node_parent[p]:
            p = self.__node_parent[p]
        return p

    def connect(self, p: int, q: int):
        p_parent, q_parent = self.__parent(p), self.__parent(q)
        if p_parent == q_parent:
            return
        if self.__size[p_parent] < self.__size[q_parent]:
            self.__node_parent[p_parent] = q_parent 
            self.__size[q_parent] += self.__size[p_parent] 
        else:
            self.__node_parent[q_parent] = p_parent 
            self.__size[p_parent] += self.__size[q_parent]   
        return

    def isConnected(self, p: int, q: int) -> bool:
        return self.__parent(p) == self.__parent(q)

    def __repr__(self):
        return " weightedQuickUnionDisjointSets "

testDisjointSets(weightedQuickUnionDisjointSets, 100000)

class weightedQuickUnionDisjointSets_PathCompression:
    def __init__(self, n:int):
        self.__node_parent = [i for i in range(n)]
        self.__size = [1] * n
        pass

    def __parent(self, p: int) -> int:
        if p == self.__node_parent[p]:
            return p
        else:
            self.__node_parent[p] = self.__parent(self.__node_parent[p])
            return self.__node_parent[p]

    def connect(self, p: int, q: int):
        p_parent, q_parent = self.__parent(p), self.__parent(q)
        if p_parent == q_parent:
            return
        if self.__size[p_parent] < self.__size[q_parent]:
            self.__node_parent[p_parent] = q_parent 
            self.__size[q_parent] += self.__size[p_parent] 
        else:
            self.__node_parent[q_parent] = p_parent 
            self.__size[p_parent] += self.__size[q_parent]   
        return

    def isConnected(self, p: int, q: int) -> bool:
        return self.__parent(p) == self.__parent(q)

    def __repr__(self):
        return " weightedQuickUnionDisjointSets_PathCompression "

testDisjointSets(weightedQuickUnionDisjointSets_PathCompression, 100000)
    
# HW Exercise 1a
for i in range(1, 6):
    print("*"*i)

# HW Exercise 1b
def drawTriangle(N: int) -> None:
    """
    :param N: The height of Triangle
    """
    for i in range(1, N+1):
        print("*"*i)

    return
drawTriangle(10)

# HW Exercise 2 & 3
class ClassNameHere:
    def __init__(self):
        pass

    def main(self):
        numbers = [9, 2, 15, 2, 22, 10, 6]
        print(self.max(numbers))
        print(self.forMax(numbers))
        return


    def max(self, data: list) -> int:
        """
        :param data: a python list of int array
        :return: the maximal element in the list
        """
        return max(data)
    
    def forMax(self, data: list) -> int:
        """
        :param data: a python list of int array
        :return: the maximal element in the list(using loop)
        """
        curr_max_element = -1
        for element in data:
            if  element > curr_max_element:
                curr_max_element = element
        return curr_max_element

tmp = ClassNameHere()
tmp.main()

# HW Exercise 4
class breakCotinue:
    def __init__(self):
        pass

    def main(self):
        a = [1, 2, -3, 4, 5, 4]
        n = 3
        print(self.windowPosSum(a,n))

    def windowPosSum(self, a: list, n: int) -> list:
        """
        :param a: a list of int array
        :param n: window size
        :return: replaces each element a[i] with the sum of a[i] through a[i + n], 
                 but only if a[i] is positive valued.If there are not enough values 
                 because we reach the end of the array, we sum only as many values as we have.
        """
        output = []
        for i, a_i in enumerate(a):
            if a_i > 0:
                cur = 0
                for j, a_j in enumerate(a[i:]):
                    if j > n:
                        break
                    cur += a_j
                output.append(cur)
            else:
                output.append(a_i)
        return output
    
tmp = breakCotinue()
tmp.main()

# Discussion 1.1
size = int(27)
name = "Fido"
class Dog:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size 
        pass

    def bark(self, times:int):
        """
        :param times: the number of barking times
        """
        for i in range(times):
            print("Barking...")
        return
    
    def play(self):
        print("playing...")
        return
    
myDog = Dog(name,size)
x = size - 5
if x < 15:
    myDog.bark(8)
while x > 3:
    x -= 1
    myDog.play()
numList = [2,4,6,8]
print("Hello ")
print("Dog: " + name)

print(numList[1])
if numList[3] == 8:
    print("potato")


# Discussion 1.2
def mystery(inputArray: list, k: int) -> int:
    x = inputArray[k]
    answer = k
    index = k + 1
    while index < len(inputArray):
        if inputArray[index] < x:
            x = inputArray[index]
            answer = index
        index = index + 1
    return answer
print(mystery([3, 0, 4, 6, 3], 2))

def mystery2(inputArray: list) -> None:
    index = 0
    while index < len(inputArray):
        targetIndex = mystery(inputArray, index)
        temp = inputArray[targetIndex]
        inputArray[targetIndex] = inputArray[index]
        inputArray[index] = temp
        index = index + 1
    return inputArray
print(mystery2([3, 0, 4, 6, 3]))

# Discussion 1.3
def fib(n: int) -> int:
    assert n >= 1, "n should be no smaller than 1"
    fib_list = [0,1]
    while len(fib_list) < n+1:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[n-1]
print(fib(5))

# python class static VS. nonstatic method
class Dog:
    weightInPounds = -1
    def __init__(self, weightInPounds):
        Dog.weightInPounds = weightInPounds
        pass

    def make_noise(self):
        print("bark!")
    
    @staticmethod
    def make_noise_static():
        print("bark!")

    @classmethod
    def weight_count(cls):
        print(cls.weightInPounds)

try:
    Dog.make_noise()
except Exception as e:
    print(e)
    
Dog.make_noise_static()
Dog(11).weight_count()

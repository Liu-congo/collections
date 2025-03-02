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
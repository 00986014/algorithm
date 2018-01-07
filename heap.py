from random import randint

class MaxHeap(object):
    def __init__(self):
        self.__nums = [0]
        self.__count = 0

    def heapify(self, nums):
        for i in xrange(len(nums)):
            self.__nums.append(nums[i])
        self.__count = len(nums)

        for i in xrange(self.__count/2, 0, -1):
            self.__shiftDown(i)

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def data(self):
        return self.__nums

    def __shiftUp(self, k):
        while k > 1 and self.__nums[k/2] < self.__nums[k]:
            self.__nums[k/2], self.__nums[k] = self.__nums[k], self.__nums[k/2]
            k /= 2

    def __shiftDown(self, k):
        while k*2 <= self.__count:
            j = k*2
            if j+1<=self.__count and self.__nums[j+1]>self.__nums[j]:
                j += 1
            if self.__nums[k] >= self.__nums[j]:
                break
            self.__nums[k], self.__nums[j] = self.__nums[j], self.__nums[k]
            k = j


    def insert(self, item):        
        self.__nums.append(item)
        self.__count += 1
        self.__shiftUp(self.__count)

    def extractMax(self):
        assert self.__count>0
        res = self.__nums[1]
        self.__nums[1], self.__nums[self.__count] = self.__nums[self.__count], self.__nums[1]
        self.__nums.pop()
        self.__count -= 1
        self.__shiftDown(1)
        return res


if __name__ == '__main__':
    maxheap = MaxHeap()
    for i in xrange(15):
        maxheap.insert(randint(0, 99))

    while not maxheap.isEmpty():
        print maxheap.extractMax()

    nums = []
    for i in xrange(15):
        nums.append(randint(0, 99))
    maxheap.heapify(nums)
    print maxheap.data()
    

        

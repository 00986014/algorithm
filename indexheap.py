#coding:utf8
from random import randint

class MaxHeap(object):
    def __init__(self):
        self.__nums = [0]
        self.__count = 0
        self.__indexes = [0]

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
        while k > 1 and self.__nums[self.__indexes[k/2]] < self.__nums[self.__indexes[k]]:
            self.__indexes[k/2], self.__indexes[k] = self.__indexes[k], self.__indexes[k/2]
            k /= 2

    def __shiftDown(self, k):
        while k*2 <= self.__count:
            j = k*2
            if j+1<=self.__count and self.__nums[self.__indexes[j+1]]>self.__nums[self.__indexes[j]]:
                j += 1
            if self.__nums[self.__indexes[k]] >= self.__nums[self.__indexes[j]]:
                break
            self.__indexes[k], self.__indexes[j] = self.__indexes[j], self.__indexes[k]
            k = j


    def insert(self, i, item):
        i += 1
        self.__nums.append(item)
        self.__indexes.append(i)
        self.__count += 1
        self.__shiftUp(self.__count)

    def extractMax(self):
        assert self.__count>0
        res = self.__nums[self.__indexes[1]]
        self.__indexes[1], self.__indexes[self.__count] = self.__indexes[self.__count], self.__indexes[1]
        self.__nums.pop()
        self.__count -= 1
        self.__shiftDown(1)
        return res

    def extractMaxIndex(self):
        assert self.__count>0
        res = self.__indexes[1] - 1
        self.__indexes[1], self.__indexes[self.__count] = self.__indexes[self.__count], self.__indexes[1]
        self.__nums.pop()
        self.__count -= 1
        self.__shiftDown(1)
        return res

    def getItem(self, i):
        return self.__nums[i+1]

    def change(self, i, newItem):
        i += 1
        self.__nums[i] = newItem

        #找到index[j]=i，j表示nums[i]在堆中的位置
        #之后shiftup(j)，再shiftdown(j)
        for j in xrange(1, self.__count+1):
            if self.__indexes[j] == i:
                self.__shiftUp(j)
                self.__shiftDown(j)
                return


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
    

        

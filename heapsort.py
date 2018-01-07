from random import randint
import time
from heap import MaxHeap

def heapSort1(nums):
    n = len(nums)
    maxheap = MaxHeap()
    for i in xrange(n):
        maxheap.insert(nums[i])

    for i in xrange(n-1, -1, -1):
        nums[i] = maxheap.extractMax()

def heapSort2(nums):
    n = len(nums)
    maxheap = MaxHeap()
    maxheap.heapify(nums)
    for i in xrange(n-1, -1, -1):
        nums[i] = maxheap.extractMax()

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    nums1 = nums[:]

    start = time.clock()
    heapSort1(nums)
    end = time.clock()
    print nums
    print (end-start)

    start = time.clock()
    heapSort2(nums1)
    end = time.clock()
    print nums1
    print (end-start)

from random import randint
import time

def selectionSort(nums):
    n = len(nums)
    for i in xrange(n):
        minindex = i
        for j in xrange(i+1, n):
            if nums[j]<nums[minindex]:
                minindex = j
        nums[minindex], nums[i] = nums[i], nums[minindex]
    return nums

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    start = time.clock()
    selectionSort(nums)
    end = time.clock()
    print nums
    print (end-start)

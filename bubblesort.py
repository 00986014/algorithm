from random import randint
import time

def bubbleSort(nums):
    n = len(nums)
    for i in xrange(n-2, -1, -1):
        for j in xrange(i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    start = time.clock()
    bubbleSort(nums)
    end = time.clock()
    print nums
    print (end-start)

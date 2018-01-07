from random import randint
import time

def __shiftDown(nums, n, k):
    while k*2+1<n:
        j = k*2+1
        if j+1<n and nums[j+1]>nums[j]:
            j += 1
        if nums[k] >= nums[j]:
            break
        nums[k], nums[j] = nums[j], nums[k]
        k = j

    
def heapSort3(nums):
    n = len(nums)
    for i in xrange((n-1)/2, -1, -1):
        __shiftDown(nums, n, i)

    for i in xrange(n-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        __shiftDown(nums, i, 0)


if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums


    start = time.clock()
    heapSort3(nums)
    end = time.clock()
    print nums
    print (end-start)

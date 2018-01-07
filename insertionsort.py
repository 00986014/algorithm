from random import randint
import time

def insertionSort(nums):
    n = len(nums)
    for i in xrange(1, n):
        for j in xrange(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    start = time.clock()
    insertionSort(nums)
    end = time.clock()
    print nums
    print (end-start)

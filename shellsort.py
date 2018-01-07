from random import randint
import time

def shellSort(nums):
    n = len(nums)
    h = 1
    while h<n/3:
        h = h*3 + 1
    while h>=1:
        for i in xrange(h, n):
            for j in xrange(i, h-1, -h):
                if nums[j] < nums[j-h]:
                    nums[j], nums[j-h] = nums[j-h], nums[j]
                else:
                    break
        h /= 3

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    start = time.clock()
    shellSort(nums)
    end = time.clock()
    print nums
    print (end-start)

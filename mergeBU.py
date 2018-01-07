from random import randint
import time

def mergeSortBU(nums):
    n = len(nums)
    size = 1
    while size<=n:
        for i in xrange(0, n, size*2):
            if i+size<n:
                __merge(nums, i, i+size-1, min(i+size*2-1, n-1))
        size *= 2


def __merge(nums, l, mid, r):
    aux = nums[l:r+1]
    i, j = l, mid+1
    for k in xrange(l, r+1):
        if i>mid:
            nums[k] = aux[j-l]
            j += 1
        elif j>r:
            nums[k] = aux[i-l]
            i += 1
        elif aux[i-l]<aux[j-l]:
            nums[k] = aux[i-l]
            i += 1
        else:
            nums[k] = aux[j-l]
            j += 1

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    start = time.clock()
    mergeSortBU(nums)
    end = time.clock()
    print nums
    print (end-start)
    

from random import randint
import time

def quickSort(nums):
    n = len(nums)
    __quickSort(nums, 0, n-1)


def __quickSort(nums, l, r):
    if l>=r:
        return

    p = __partition(nums, l, r)
    __quickSort(nums, l, p-1)
    __quickSort(nums, p+1, r)

def __partition(nums, l, r):
    k = randint(l, r)
    nums[l], nums[k] = nums[k], nums[l]
    v = nums[l]
    i, j = l+1, r
    while True:
        while i<=r and nums[i]<v:
            i += 1
        while j>=l+1 and nums[j]>v:
            j -= 1
        if i>j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        
    nums[l], nums[j] = nums[j], nums[l]
    return j

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    start = time.clock()
    quickSort(nums)
    end = time.clock()
    print nums
    print (end-start)
    

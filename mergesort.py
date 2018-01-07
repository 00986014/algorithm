#coding:utf8
from random import randint
import time

def mergeSort(nums):
    __mergeSort(nums, 0, len(nums)-1)
    

def __mergeSort(nums, l, r):
    if l>=r:
        return

    mid = (l+r)/2
    __mergeSort(nums, l, mid)
    __mergeSort(nums, mid+1, r)
    # 近乎有序的情况下，可增加这一条if语句
    if nums[mid]>nums[mid+1]:
        __merge(nums, l, mid, r)


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
    mergeSort(nums)
    end = time.clock()
    print nums
    print (end-start)
    

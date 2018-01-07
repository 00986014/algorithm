from random import randint
import time

def quickSort3Ways(nums):
    n = len(nums)
    __quickSort3Ways(nums, 0, n-1)


def __quickSort3Ways(nums, l, r):
    if l>=r:
        return    
    
    k = randint(l, r)
    nums[l], nums[k] = nums[k], nums[l]
    v = nums[l]
    
    lt, gt, i = l, r+1, l+1
    while i<gt:
        if nums[i]<v:
            nums[i], nums[lt+1] = nums[lt+1], nums[i]
            i += 1
            lt += 1
        elif nums[i]>v:
            nums[i], nums[gt-1] = nums[gt-1], nums[i]
            gt -= 1
        else:
            i += 1
            
    nums[l], nums[lt] = nums[lt], nums[l]
    
    __quickSort3Ways(nums, l, lt-1)
    __quickSort3Ways(nums, gt, r)

if __name__ == '__main__':
    nums = []
    for i in range(50):
        nums.append(randint(0, 100))
    print nums

    start = time.clock()
    quickSort3Ways(nums)
    end = time.clock()
    print nums
    print (end-start)
    

import random as r
nums = [r.randint(1, 50) for x in range(10)]
print('list : ', nums)


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


print('list sorted : ', bubble_sort(nums))
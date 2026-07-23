import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        left = []
        right = []
        left_mult, right_mult = 1, 1
        for i in range(len(nums)):
            #1-> 1-> 2-> 8 [1,1,2,8]
            left.append(left_mult)
            left_mult *= nums[i]
            #1 -> [6,1]... [48,24,6,1]
            right.insert(0, right_mult)
            right_mult *= nums[-1-i]


        for i in range(len(nums)):
            new_list.append(left[i]*right[i])


        return new_list

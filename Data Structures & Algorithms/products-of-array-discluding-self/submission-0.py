import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            new_list.append(math.prod(nums[:i])*math.prod(nums[i+1:]))

        return new_list
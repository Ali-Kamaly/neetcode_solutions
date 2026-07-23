class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            current_val = nums[i]
            other_num = target-current_val
            if other_num not in vals:
                vals[current_val] = i
            else:
                return [vals.get(other_num), i] 

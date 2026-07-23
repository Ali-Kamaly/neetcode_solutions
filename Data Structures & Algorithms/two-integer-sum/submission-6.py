class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            other_num = target-nums[i]
            if other_num not in vals:
                vals[nums[i]] = i
            else:
                return [vals.get(other_num), i] 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            if target-nums[i] not in vals:
                vals[nums[i]] = i
            else:
                return [vals.get(target-nums[i]), i] 

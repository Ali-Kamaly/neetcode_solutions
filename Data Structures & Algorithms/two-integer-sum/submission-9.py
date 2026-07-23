class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals_seen = {}
        for i in range(len(nums)):
            num_needed = target - nums[i]
            if num_needed in vals_seen:
                return [vals_seen[num_needed], i] 
            else:
                vals_seen[nums[i]] = i
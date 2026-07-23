class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals_seen = {}

        for i, n in enumerate(nums):
            num_needed = target - n
            if num_needed in vals_seen:
                return [vals_seen[num_needed], i]
            vals_seen[n] = i


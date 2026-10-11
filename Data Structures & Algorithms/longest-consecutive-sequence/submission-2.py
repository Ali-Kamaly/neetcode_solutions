class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_sequence_length = 0

        for x in num_set:
            if x-1 not in num_set:
                sequence_length = 1
                while x+1 in num_set:
                    sequence_length +=1 
                    x = x+1
                if sequence_length>max_sequence_length:
                    max_sequence_length = sequence_length

        return max_sequence_length
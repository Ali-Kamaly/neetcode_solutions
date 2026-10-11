class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #using set for O(1) lookups
        numSet = set(nums)
        maxLength = 0
        for x in numSet:
            currentLength = 1
            if x-1 not in numSet:
                #i.e. x is the absolute beginning of its sequential chain
                while x+1 in numSet:
                    currentLength+=1
                    x = x+1
                maxLength = max(currentLength, maxLength)

        return maxLength


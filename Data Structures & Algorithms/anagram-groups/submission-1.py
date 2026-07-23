class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0]*26

            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            
            signature = tuple(count)
            if signature not in groups:
                groups[signature] = []
            
            groups[signature].append(word)
        
        return list(groups.values())
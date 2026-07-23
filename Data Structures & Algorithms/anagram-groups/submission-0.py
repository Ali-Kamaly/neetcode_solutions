class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        # letters = {{'b': 2, 'c': 5}, {'b': 2, 'c': 5], {'a': 5, 't': 52}}

        for word in strs:
            count = [0] * 26

            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1

            key = tuple(count)
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
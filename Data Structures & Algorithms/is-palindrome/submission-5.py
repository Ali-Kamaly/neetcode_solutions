class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for i in s:
            if i.isalnum() and i != ' ':
                string.append(i.lower())
        new_string = []
        for i in range(len(string)):
            new_string.append(string[-(i+1)])
        
        return str(new_string) == str(string)
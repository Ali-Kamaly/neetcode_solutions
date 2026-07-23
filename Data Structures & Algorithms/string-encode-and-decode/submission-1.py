class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + '#' + string

        return encoded_str

        'hi','kamaly'
        '2#hi6#kamaly'

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        while s!= "":
            hash_index = s.index('#')
            str_length = int(s[:hash_index])
            end_of_string_index = hash_index + str_length + 1

            string = s[hash_index+1:end_of_string_index]
            decoded_str.append(string)

            s = s[end_of_string_index:]    

        return decoded_str
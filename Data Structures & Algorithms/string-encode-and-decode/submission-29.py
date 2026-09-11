class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for val in strs:
            encoded_str += str(len(val)) + '#' + val
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        last_number_index_start = 0

        for index in range(len(s)):
            if s[index] == '#' and index > last_number_index_start:
                word_length = int(s[last_number_index_start : index])
                word_ends_at = index + word_length
                result.append(s[index + 1 : word_ends_at + 1])
                last_number_index_start = word_ends_at + 1
        return result
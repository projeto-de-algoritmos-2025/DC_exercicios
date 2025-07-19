class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result_chars = []
        n = len(s)
        for i in range(0, n, k):
            substring = s[i:i + k]
            current_sum = 0
            for char in substring:
                current_sum += ord(char) - ord('a')
            hashed_char_index = current_sum % 26
            new_char = chr(hashed_char_index + ord('a'))
            result_chars.append(new_char)
        return "".join(result_chars)

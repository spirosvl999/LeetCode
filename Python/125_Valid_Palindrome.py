class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain_str = ""

        for c in s:
            if c.isalnum():
                plain_str += c.lower()
                                                                            # Runtime: 7 ms // Beats 81.86%
        return plain_str == plain_str[::-1]                                 # Memory: 18.18 MB // Beats 55.65%

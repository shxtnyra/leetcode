class Solution:
    def longestPalindrome(self, s: str) -> str:
        window_size = len(s)

        while window_size > 0:
            for i in range(len(s) - window_size + 1):
                if self.checkPalindrome(s[i:i+window_size]):
                    return s[i:i+window_size]

            window_size -= 1
        return ""

    def checkPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("a"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("gabagdc"))
print(sol.longestPalindrome("abacca"))
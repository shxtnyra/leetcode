class Solution:
    def bruteforce(self, s: str) -> int:
        chars = set()
        max_len = 0
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                if s[j] in chars:
                    chars.clear()
                    break
                chars.add(s[j])
                count += 1
            max_len = count if count > max_len else max_len
        return max_len

    def optimal(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_index:
                char_index.pop(s[left])
                left += 1

            char_index[s[right]] = right
            max_len = (right - left + 1) if (right - left + 1) > max_len else max_len

        return max_len

    def optimal2(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            char_index[s[right]] = right
            max_len = (right - left + 1) if (right - left + 1) > max_len else max_len

        return max_len


sol = Solution()
text = "a"
print(text)
print(sol.optimal2(text))

text = "aa"
print(text)
print(sol.optimal2(text))

text = "abcabcbb"
print(text)
print(sol.optimal2(text))

text = "bbbbb"
print(text)
print(sol.optimal2(text))

text = "pwwkew"
print(text)
print(sol.optimal(text))
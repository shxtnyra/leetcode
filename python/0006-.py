class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cursor: int = 0
        step: int = -1
        rows = [""] * len(s)
        for i in range(len(s)):
            rows[cursor] += s[i]
            if cursor == 0 or cursor == numRows - 1:
                step = -step

            cursor += step

        return "".join(rows)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        low, high = 0, len(nums1)
        half_len = (len(nums1) + len(nums2) + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            num1_left = nums1[i-1] if i > 0 else float('inf')
            num1_right = nums1[i] if i < len(nums1) else float('inf')
            num2_left = nums2[j-1] if j > 0 else float('inf')
            num2_right = nums2[j] if j < len(nums2) else float('inf')

            if num1_left <= num1_right and num2_left <= num1_right:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(num1_left, num2_left) + min(num1_right, num2_right)) / 2.0
                else:
                    return float(max(num1_left, num2_left))

            elif num1_left > num2_right:
                high = i - 1
            else:
                low = i + 1
        return None


sol = Solution()
print(sol.findMedianSortedArrays([2,3,12,14,50], [4,7,9,11,22,30]))








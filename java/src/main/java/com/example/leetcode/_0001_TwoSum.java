package com.example.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class _0001_TwoSum {
    public int[] optimal(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[] { seen.get(complement), i };
            }
            seen.put(nums[i], i);
        }
        return null;
    }

    public static void main(String[] args) {
        _0001_TwoSum sol = new _0001_TwoSum();

        System.out.println(Arrays.toString(sol.optimal(new int[]{2, 7, 11, 15}, 9))); // [0, 1]
        System.out.println(Arrays.toString(sol.optimal(new int[]{3, 2, 4}, 6)));      // [1, 2]
        System.out.println(Arrays.toString(sol.optimal(new int[]{3, 3}, 6)));         // [0, 1]
    }
}
package com.example.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class _0003_LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> seen = new HashMap<>();
        int left = 0;
        int max_len = 0;

        for (int right = 0; right < s.length(); right++) {
            if (seen.containsKey(s.charAt(right)) && seen.get(s.charAt(right)) >= left) {
                left = seen.get(s.charAt(right)) + 1;
            }
            seen.put(s.charAt(right), right);
            max_len = Math.max((right - left + 1), max_len);
        }

        return max_len;
    }

    public static void main(String[] args) {
        _0003_LongestSubstringWithoutRepeatingCharacters sol = new _0003_LongestSubstringWithoutRepeatingCharacters();

        System.out.println(sol.lengthOfLongestSubstring("a"));
        System.out.println(sol.lengthOfLongestSubstring("aa"));
        System.out.println(sol.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(sol.lengthOfLongestSubstring("bbbbb"));
        System.out.println(sol.lengthOfLongestSubstring("pwwkew"));

    }
}

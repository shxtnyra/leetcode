/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const seen_dict = {}
    let left = 0
    let max_len = 0
    for (let right = 0; right < s.length; right++) {
        if (s[right] in seen_dict && seen_dict[s[right]] >= left) {
            left = seen_dict[s[right]] + 1;
        }
        seen_dict[s[right]] = right;
        max_len = (right - left + 1) > max_len ? (right - left + 1) : max_len;
    }

    return max_len;
};

console.log(lengthOfLongestSubstring("a"));
console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
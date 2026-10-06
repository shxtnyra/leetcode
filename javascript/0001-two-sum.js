/**
 * https://leetcode.com/problems/two-sum/
 * Даны массив целочисленных значений nums и целое число target,
 * верните индексы двух таких чисел, которые в сумме равны target.
 * 
 * Гарантируется, что каждый ввод имеет ровно одно решение.
 * Также учтите, что вы не можете использовать одно и то же число дважды.
 * 
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = {};
    for (let i = 0; i < nums.length; i++) {
        complement = target - nums[i];
        if (complement in seen)
            return [seen[complement], i];
        seen[nums[i]] = i;
    }
    return null;
};

console.log(twoSum([2, 7, 11, 15], 9))
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
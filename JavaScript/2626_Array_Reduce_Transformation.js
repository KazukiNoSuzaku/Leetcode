/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let acc = init;
    for (const num of nums) {
        acc = fn(acc, num);
    }
    return acc;
};

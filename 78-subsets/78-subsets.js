/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    res = []
    helper(0, nums, [], res)
    return res
};

function helper(i, nums, path, res) {
    if (i == nums.length) {
        res.push(path.slice())
        return
    }
    helper(i + 1, nums, path, res)
    path.push(nums[i])
    helper(i + 1, nums, path, res)
    path.pop()
}
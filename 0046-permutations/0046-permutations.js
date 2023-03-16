/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    return permutation(nums)
};

function permutation(nums) {
    if (nums.length === 1) {
        return [nums]
    }
    
    const result = []
    
    for (const num of nums) {
        const cases = permutation(nums.filter(item => item !== num))
        
        cases.forEach(c => result.push([num].concat(c)))
    }
    
    return result
}
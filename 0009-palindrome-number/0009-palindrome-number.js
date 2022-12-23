/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0) {
        return false
    }

    const stringified = String(x)
    return stringified === stringified.split('').reverse().join('')
};
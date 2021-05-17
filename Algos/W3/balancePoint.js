
/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

// const nums1 = [-2, 5, 7, 0, 3];
// const expected1 = 2;

// const nums2 = [9, 9];
// const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
    if (nums.length < 3) {
        return -1
    }

    let left = nums[0]
    let right = 0

    // calculate the right to be the total sum
    for (let i = 2; i < nums.length; i++) {
        right += nums[i]
        console.log(right);
    }

    for (let i = 1; i < nums.length; i++) {
        console.log(`left: ${left}`);
        console.log(`right: ${right}`);
        if (left === right) {
            return i
        }
        right -= nums[i + 1]
        left += nums[i]
    }
    return -1
}

// console.log(balanceIndex(nums1));

/**
 * - Time: O(2n) linear -> O(n).
 * - Space: O(1) constant.
 */


// **********************************************************************
// **********************************************************************
// **********************************************************************


/* 
  Balance Point
  Write a function that returns whether the given
  array has a balance point BETWEEN indices, 
  where one side’s sum is equal to the other’s. 
*/

const nums1 = [1, 2, 3, 4, 10];
const expected1 = true;
// Explanation: between indices 3 & 4

const nums2 = [1, 2, 4, 2, 1];
const expected2 = false;

/**
 * Determines if there is a balance point BETWEEN indexes where the sum of the
 *    left side is equal to the sum of the right side of the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {boolean} Indicates if a balance point exists.
 */
function balancePoint(nums) {
    if (nums.length < 2) {
        return false
    }

    let left = nums[0]
    let right = 0

    // calculate the right to be the total sum
    for (let i = 1; i < nums.length; i++) {
        right += nums[i]
        console.log(right);
    }

    for (let i = 1; i < nums.length; i++) {
        console.log(`left: ${left}`);
        console.log(`right: ${right}`);
        if (left === right) {
            return true
        }
        right -= nums[i]
        left += nums[i]
    }
    return false
}

console.log(balancePoint(nums1));
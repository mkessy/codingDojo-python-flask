/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
  what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [1, 5, 1, 4, 5, 1, 5];
const expected5 = [5, 1];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */

function arrayMode(arr){
    var dict = {}
    var frequency = 0
    var output = []
    var allSame = true
    for (let i = 0; i < arr.length; i++){
        dict.hasOwnProperty(arr[i]) ? dict[arr[i]]++ : dict[arr[i]] = 1

        if (dict[arr[i]] > frequency){
            frequency = dict[arr[i]]
        }
        // if (!(arr[i] in dict)) {
        //     dict[arr[i]] = 1
        // } else {
        //     dict[arr[i]] += 1
        // }
    }
    for(let key in dict){
        if (dict[key] == frequency){
            // frequency = dict[key]
            output.push(Number(key))
        } else {
            allSame = false
        }
    }

    // if (frequency < 2){
    //     output = []
    // }

    return allSame ? [] : output
}

// console.log(arrayMode(nums5));

// *********************************************************************

/* 
  Missing Value
  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  Quickly determine and return the missing value.
*/

const nums12 = [3, 0, 1];
const expected12 = 2;

const nums22 = [3, 0, 1, 2];
const expected22 = null;
// Explanation: nothing is missing

/* 
  Bonus: now the lowest value can now be any integer (including negatives),
  instead of always being 0. 
*/

const nums32 = [2, -4, 0, -3, -2, 1];
const expected32 = -1;

const nums42 = [5, 2, 7, 8, 4, 9, 3];
const expected42 = 6;

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums) {
    if (unorderedNums.length < 1){
        return null
    }

    let min = unorderedNums[0]
    let max = unorderedNums[0]
    let sum = 0
    let expectedSum = 0

    unorderedNums.forEach(item => {
        if (item < min){
            min = item
        } else if (item > max){
            max = item
        }
        // console.log(`min: ${min} | max: ${max}`);
        sum += item
    });

    for (let i=min; i<=max; i++){
        expectedSum += i 
    }
    // console.log(`expectedSum: ${expectedSum} | sum: ${sum}`);

    return sum === expectedSum ? null : expectedSum - sum


    // no missing values
}

console.log(missingValue(nums32));

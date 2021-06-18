/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

// const str = "Hello World";

// const rotateAmnt1 = 0;
// const expected1 = "Hello World";

// const rotateAmnt2 = 1;
// const expected2 = "dHello Worl";

// const rotateAmnt3 = 2;
// const expected3 = "ldHello Wor";

// const rotateAmnt4 = 4;
// const expected4 = "orldHello W";

// const rotateAmnt5 = 13;
// const expected5 = "ldHello Wor";

// // Edge case
// const rotateAmnt6 = -4;
// var str2 = ""

// Test to make sure that the given parameters are a string and an int, if not return false

/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
// function rotateStr(str, amnt) {
//     if (amnt < 0){
//         return false
//     }
//     const rotateAmnt = amnt % str.length
//     return (
//         str.slice(str.length - rotateAmnt) + str.slice(0, str.length - rotateAmnt)
//     )
// }

// console.log(rotateStr(str, 13));

// function rotateStr(str, amnt) {
//     const rotateAmnt = amnt % str.length
//     let charsToRotate = ""
//     let newStr = ""

//     for (let i=str.length - rotateAmnt; i < str.length; i++){
//         charsToRotate += str[i]
//     }

//     for (let i=0; i < str.length - rotateAmnt; i++){
//         newStr += str[i]
//     }
//     return charsToRotate + newStr
// }

// console.log(rotateStr(str, 13));

// ***********************************************************************************************************
// ***********************************************************************************************************

/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strB1 = "CDAB";
const expected1 = true;
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated

const strA2 = "ABCD";
const strB2 = "CDBA";
const expected2 = false;
// Explanation: all same letters in 2nd string, but out of order

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */

/*
ABCD
CDABCDAB
*/

function isRotation(s1, s2) {
    if (s1.length !== s2.length) {
        return false
    }
    return (s1 + s1).includes(s2)
}

console.log(isRotation(strA2, strB2));
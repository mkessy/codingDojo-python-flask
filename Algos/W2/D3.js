/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "helloollo";
const expected3 = "helo";

const str4 = "abcABCabc";
const expected4 = "abcABC";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    let newStr = ""
    let seen = {}

    for (let i=str.length - 1; i>=0; i--){
        if (!seen[str[i]]){
            newStr = str[i] + newStr
            seen[str[i]] = true
        }
    }
    return newStr
}

console.log(stringDedupe(str1));


// {
//     "a" = true,
//     "b" = true
// }
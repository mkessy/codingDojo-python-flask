/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "abcABCabc"

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */

/*
1. create a function that takes in a string
2. create a newStr variable
3. create an empty dict of "seen" char
4. loop through the str 
5. if char is in seen dict then do nother
6. if char is not in seen dict then we add to the dict and the newStr
*/

function stringDedupe(str) {
    let newStr = ""
    let seen = {}

    for (let i=str.length - 1; i>0; i--){
        if(!seen[str[i]]){
            seen[str[i]] = true
            newStr = str[i] + newStr
        }
    }
    return newStr
}

console.log(stringDedupe(str3));
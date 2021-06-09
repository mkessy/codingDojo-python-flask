/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

// const str1 = " there's no free lunch - gotta pay yer way. ";
// const expected1 = "TNFL-GPYW";

// const str2 = "Live from New York, it's Saturday Night!";
// const expected2 = "LFNYISN";

/*
1. to create a function that takes in a string
1.5 create new var called "acronym" (a blank string)
2. use .split to convert into an array
3. loop through each item
4. grab the first char of each item
5. add to "acronym"
6. capitalize all chars in var acronym 
7. return acronym
*/

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The given str converted into an acronym.
 */
// function acronymize(str) {}


// ************************************************


/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

/*
1. create a function that takes in a string
2. create new blank string var 
3. loop through string starting in the back
4. add it to the new string var
5. return the new string var
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    var reversed = ""
    for (let i=str.length - 1; i>=0; i--){
        reversed += str[i]
    }
    return reversed
}

console.log(reverseString(str2));
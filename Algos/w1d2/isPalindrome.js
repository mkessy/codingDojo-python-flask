 
/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

//   const str1 = "a x a";
//   const expected1 = true;
  
//   const str2 = "racecar";
//   const expected2 = true;
  
//   const str3 = "Dud";
//   const expected3 = false;
  
//   const str4 = "oho!";
//   const expected4 = false;
  
  /**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */

  /*
1. build a function that take in a string
2. reverse string into a new string
3. compare both string
4. return true of false depending
  */

  function isPalindrome(str) {
      if (str.length == 0){
          return false
      }

      var newStr = ""
      for(let i=str.length-1; i>=0; i--){
        newStr += str[i]
      }
    // var newStr = str.split('').reverse().join('')
    console.log(newStr);
    //   if (str === newStr){
    //       return true
    //   }
      
      return str === newStr
  }

// //   O(n/2) -> O(n)
//   function isPalindrome2(str) {
//     for (let i=0; i < Math.floor(str.length / 2); i++){
//         let leftChar = str[i]
//         let rightChar = str[str.length - 1 - i]

//         if(leftChar !== rightChar){
//             return false
//         }
//     }
//     return true
//   }

//   console.log(isPalindrome2(str1));
  
  // ******************************************************************************
  // ******************************************************************************
  // ******************************************************************************
  
  /* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
  */
  
  const str1 = "what up, daddy-o?";
  const expected1 = "dad";
  
  const str2 = "uh, not much";
  const expected2 = "u";
  
  const str3 = "Yikes! my favorite racecar erupted!";
  const expected3 = "e racecar e";
  
  /**
   * Finds the longest palindromic substring in the given string.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {string} The longest palindromic substring from the given string.
   */

  /*
1. build a function that takes in a string
2. have something to hold onto the longest PAL 
3. start at the begining and at the end and compare to see if it is a PAL
4. if NO: decrement ending pos by one  if YES: save as longest PAL
5. after end reaches the start increase start pos by 1 repeate steps 3 and 4
  */
  function longestPalindromicSubstring(str) {
      if (str.length === 0){
          return false
      }

      let longestPAL = str[0]
      for (let startIndex=0; startIndex<str.length; startIndex++){
            for (let endIndex=str.length-1; endIndex >= startIndex; endIndex--){
                let subStr = str.slice(startIndex, endIndex)
                console.log(subStr);

            if (subStr.length > longestPAL.length && isPalindrome(subStr)){
                console.log(`setting ${subStr} to be the longest PAL`);
                longestPAL = subStr
            }
          }
      }
      return longestPAL
  }
  
console.log(longestPalindromicSubstring(str1));
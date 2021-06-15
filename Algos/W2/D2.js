/* 
  Parens Valid
	Given an str that has parenthesis in it
	return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the underlined ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing

const str5 = "azyx(b))(c";
const expected5 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing

const str6 = "(()())()";
const expected6 = true;
// Explanation: same number of opens and closes but the 2nd closing closes nothing

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */

 function parensValid(str) {
    var counter = 0;
    for (i = 0; i < str.length; i++){
      if (counter < 0) {
        return false
      }
      if (str[i] === "(") {
          console.log("plus 1");
          counter++
      }
      if (str[i] === ")") {
        console.log("minus 1");
        counter--
        }
    }
    return counter === 0
  }
//   var answer = parensValid(str1)
//   console.log(answer)
  
// ********************************************
// ********************************************
// ********************************************

/* 
  Braces Valid
  Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str10 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected10 = true;

const str11 = "D(i{a}l[ t]o)n{e";
const expected11 = false;

const str12 = "A(1)s[O (n]0{t) 0}k";
const expected12 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var stack = []
    var closeToOpoen = {
        ')':'(', 
        ']':'[',
        '}':'{'
    }
    for (let i=0; i < str.length; i++){
        switch (str[i]) {
            case '(':
            case '{':
            case "[":
                stack.push(str[i])
                break;
            case ')':
            case '}':
            case "]":
                if (closeToOpoen[str[i]] === stack[stack.length - 1]){
                    stack.pop()
                } else {
                    return false
                }
                break
        }
    }
    return stack.length === 0
}

// console.log(bracesValid(str12));

function bracesValid2(str){
    var stack = []
    var openToClose = {
        '(':')', 
        '[':']',
        '{':'}'
    }

    for (let i=0; i<str.length; i++){
        console.log("***************");
        console.log(`str[i]: ${str[i]}`);
        console.log(`if: ${str[i] in openToClose}`);
        console.log(`else: ${str[i] in Object.values(openToClose)}`);
        if (str[i] in openToClose) {
            stack.push(str[i])
        } else if (str[i] in Object.values(openToClose)) {
            console.log(`str: ${str[i]} || last stack item: ${stack[stack.length -1]}`);
            if (stack[stack.length -1] === str[i]){
                stack.pop()
            } else {
                return false
            }
        }
        console.log(`stack: ${stack}`);
    }
    return stack.length === 0
}

console.log(bracesValid2(str1));
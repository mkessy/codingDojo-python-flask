/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

  const keys1 = ["abc", 3, "yo"];
  const vals1 = [42, "wassup", true];
  const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
  };
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */

function zipArraysIntoMap(keys, values) {
    const hashMap = {};
  
    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        const val = values[i];
        
        if (val in hashMap){
          return false
          }
  
      hashMap[key] = val;
    }
    return hashMap;
  }

//   ****************************************************

/* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

// const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
// const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

const obj1 = { name: "Zaphod", first_name: "Zaphod", charm: "high", morals: "dicey" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/*
1. create a function that takes in a object1
1. create a emtpy new object2
1. loop through the keys of the object1
1. if the value of the key is already in the object2....
  - return false
1. set the value of the key at object1 to be the key in object2 with the value of object2 being the key of object1 
*/

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {
    var newObj = {}
    // var keys = Object.values(obj)
    // console.log(keys);
    for (let key in obj){
        let value = obj[key]

        if (value in newObj){
            return false
        }

        newObj[value] = key
    }
    return newObj
}

console.log(invertObj(obj1));
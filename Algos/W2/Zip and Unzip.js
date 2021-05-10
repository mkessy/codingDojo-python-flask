/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */
/*
1. create a function that takes in two arrays
2. check to make sure both arrays are the same length - edge case
3. create a new dict
4. loop over both arrays 
5. assign key[i] with the value of val[i]

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
      if(keys.length !== values.length){
          console.log("cannot zip together because they are diffent lengths");
          return false
      }
      let zipped = {}
      for (let i=0; i<keys.length; i++){
          zipped[keys[i]] = values[i]
      }
      return zipped
  }

//   console.log(zipArraysIntoMap(keys1, vals1));

// **************************************************************************************************************************************************
// **************************************************************************************************************************************************
// **************************************************************************************************************************************************

  /* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj2 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected2 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
/*
1. create a function that takes in a dictionary 
2. create a new dict
3. grab all the keys
4. loop through the keys
5. assign the value for that key as the key and the key as the value
6. return the new dict
*/
function invertObj(obj) {
    let new_dict = {}
    let all_keys = Object.keys(obj)
    all_keys.forEach(key => {
        new_dict[obj[key]] = key
    });
    // for(let key in obj){
    //   new_dict[obj[key]] = key
    // }
    return new_dict
}

console.log(invertObj(obj2));
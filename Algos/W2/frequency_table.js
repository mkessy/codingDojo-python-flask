/* 
  Given an array of strings
  return a sum to represent how many times each array item is found (a frequency table)
  Useful methods:
    Object.hasOwnProperty("keyName")
      - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */

/*
1. create a function that takes in a array
2. create a new obj
3. iterate through our array
4. check to see if item already exists in new obj
5. if YES: then add one to count || if NO: then create item and set value to 1
6. return the new obj
*/

function frequencyTableBuilder(arr) {
    let frequencyTable = {}
    // for (let i=0; i<arr.length; i++){
    //     console.log(arr[i]);
    // }
    
    // for (let item of arr){
        //     console.log(item);
        // }
    
    arr.forEach(item => {
        if (frequencyTable.hasOwnProperty(item)){
            frequencyTable[item]++
        } else {
            frequencyTable[item] = 1
        }
    });
    return frequencyTable
}


console.log(frequencyTableBuilder(arr3));

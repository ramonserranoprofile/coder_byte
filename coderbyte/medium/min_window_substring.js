// define min window substring function
function MinWindowSubstring(strArr) {
    // define variables
    let str = strArr[0];
    let substr = strArr[1];
    let min = str.length + 1;
    let result = '';
    // loop through the string
    for (let i = 0; i < str.length; i++) {
        // loop through the string
        for (let j = i + 1; j < str.length + 1; j++) {
        // define substring
        let sub = str.slice(i, j);
        // check if substring length is less than min and includes all characters
        if (sub.length < min && substr.split('').every((char) => sub.includes(char))) {
            min = sub.length;
            result = sub;
        }
        }
    }
    // return result
    return result;
    }
    // keep this function call here 
console.log(MinWindowSubstring(["aabdccdbcacd", "aad"]));
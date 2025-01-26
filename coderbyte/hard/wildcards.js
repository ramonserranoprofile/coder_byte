// Have a function WildCard(str) read str which will contain two strings separated by a space. The first string will consist of the following sets of characters: +, *, $, and {N} which is optional. The plus (+) character represents a single alphabetic character, the asterisk (*) represents a sequence of zero or more alphabetic characters, the dollar sign ($) represents a sequence of one or more alphabetic characters, and N represents a single digit. Your goal is to determine if the second string exactly matches the pattern of the first string and if it does, return the string true, otherwise return the string false.

// For example: if str is "++*{5} gheeeee" then the second string in this case does match the pattern, so you should return the string true. If the second string does not match the pattern, you should return the string false.
// Examples
// Input: "+*{2} mmmrrrkbb"
// Output: true
// Input: "++*{5} gheeeee"
// Output: false

function WildCard(str) {
    var arr = str.split(" ");
    var pattern = arr[0];
    var test = arr[1];
    var regex = "";
    for (var i = 0; i < pattern.length; i++) {
        if (pattern[i] === "+") {
            regex += "[a-z]";
        }
        if (pattern[i] === "$") {
            regex += "[1-9]";
        }
        if (pattern[i] === "*") {
            if (pattern[i + 1] === "{") {
                regex += '.{' + pattern[i + 2] + '}';
            } else {
                regex += '.{3}';
            }
        }
    }
    return regex = new RegExp("^" + regex + "$").test(test);
}

const readline = () => "+++++* abcdhhhhhh";
// keep this function call here
console.log(WildCard("$**+*{2} 9mmmrrrkbb")); // Output: false
console.log(WildCard(readline())); // Output: true
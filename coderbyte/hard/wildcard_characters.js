// Difficulty: Hard
// Wildcard Characters
// Have the function WildcardCharacters(str) read str which will contain two strings separated by a space. The first string will consist of the following sets of characters: +, *, and $ representing a positive digit, any character, and a number, respectively. The second string will consist of a string of characters that will be in a similar format as the first string, meaning it will also contain only +, *, and $ characters. Your goal is to determine if the second string matches the pattern of the first string. For example: if str is "+*+*" and "abcd" then the output should return true because the second string matches the pattern. If the second string does not match the pattern, return false.
// Examples
// Input: "+* abcdemmmmmm"
// Output: true
// Input: "+* abcd"
// Output: false

function WildcardCharacters(str) {
    // Dividir el input en patrón y cadena
    let [pattern, input] = str.split(" ");

    // Convertir el patrón en una expresión regular
    const regexSource = pattern
        .replace(/\+/g, "[a-zA-Z]") // "+" → cualquier letra
        .replace(/\*/g, ".*")       // "*" → cualquier número de caracteres
        .replace(/\$/g, "\\d");     // "$" → cualquier dígito

    // Crear una expresión regular que valide toda la cadena
    const regex = new RegExp(`^${regexSource}$`); // Coincidencia exacta

    // Probar si el input coincide con el patrón
    return regex.test(input);
}
//keep this function call here
const readline = () => "$**+*{2} 9mmmrrrkbb 9mrrrbbb";

console.log(WildcardCharacters(readline()));
// Input: "++*{5} abcde aabcde" Output: true
// Input: "$**+*{2} 9mmmrrrkbb 9mrrrbbb" Output: false
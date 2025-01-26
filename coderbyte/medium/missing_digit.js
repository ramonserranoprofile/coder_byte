// Find the missing digit in the equation
// Have the function missingDigit(str) take the str parameter, which will be a simple mathematical formula with three numbers, and set of arithmetic operators: +, -, *, and /. The formula will be missing one digit, and your goal is to find out what that digit is. For example, if str is "3 * 2 = 1?" then your program should output 4, because 3 * 2 = 6, which is the number that when placed in the third spot of the equation, will make the equation true.
// Examples
// Input: "38 * 2 = 8?" Output: 4
// Input: "?3 + 12 = 15" Output: 0

// define missing digit function in adding, subtracting, multiplying, and dividing, in multiplying consider exceptions.


function missingDigit(str) {
    // Parse the input string
    const [left, result] = str.split(" = ");

    // Define operators and locate the operator in the left-hand side
    const operators = ["+", "-", "*", "/"];
    let operator, parts;

    for (let op of operators) {
        if (left.includes(op)) {
            operator = op;
            parts = left.split(` ${op} `);
            break;
        }
    }

    // Extract the left-hand operand, right-hand operand, and the result
    const [operand1, operand2] = parts;
    const target = parseInt(result, 10);

    // Define a function to compute based on the operator
    const calculate = (a, b, op) => {
        switch (op) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b; 
            if (a % b !== 0) return null;
            else if (a % b === 0) return a * b;
            else return null;
            case "/": return a / b;
                if (b === 0) return null;
            else return Math.floor(a / b);            
        }
    };

    // Loop through 0-9 to find the missing digit
    for (let i = 0; i <= 9; i++) {
        const replacedOperand1 = operand1.replace("?", i);
        const replacedOperand2 = operand2.replace("?", i);

        const num1 = parseFloat(replacedOperand1);
        const num2 = parseFloat(replacedOperand2);

        // Calculate and check if it matches the target
        if (!isNaN(num1) && calculate(num1, num2, operator) === target) {
            return i; // Found the missing digit
        }

        if (!isNaN(num2) && calculate(num1, num2, operator) === target) {
            return i; // Found the missing digit
        }
    }

    return null; // Return null if no solution found
}

    
// keep this function call here
console.log(missingDigit("1? + 3 = 17")); // Output: 4
console.log(missingDigit("12 - ? = 5"));  // Output: 7
console.log(missingDigit("4? * 2 = 84")); // Output: 2
console.log(missingDigit("3? + 12 = 15"));   // Output: null
console.log(missingDigit("10 * ? = 90"));   // Output: 9


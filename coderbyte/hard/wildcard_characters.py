# Difficulty: Hard
# How to solve: I split the string by the * character and then check the length of the first and second string. If the length of the first string is equal to the length of the second string, then I return true. If the length of the first string plus the length of the third string is equal to the length of the second string, then I return true. Otherwise, I return false.
# Tags: string manipulation
# Based on these examples build the function WildcardCharacters(str) 
# example: "abcde" => false
# example: "abcde*f" => true
# example: "abc*def" => true 

def wildcard_characters(string):
    string = string.split('*')
    # based on this example: "abc*def" => true  AND "abcde*f" => true Y NO ES CON EL TEMA DE LAS LONGITUDES SINO QUE LAS LETRAS SIGAN EL ORDEN DE LA PRIMERA PARTE A LA IZQUIERDA DEL * EN LA SEGUNDA PARTE A LA DERECHA DEL *
    if len(string[0]) == len(string[1]):
        return True
    elif len(string[0]) + len(string[1]) == len(string[1]):
        return True
    else:
        return False
    




    
    
# keep this function call here
print(wildcard_characters(input()))
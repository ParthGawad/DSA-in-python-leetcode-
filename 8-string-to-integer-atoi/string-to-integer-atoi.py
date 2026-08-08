class Solution:
    def myAtoi(self, s: str) -> int:
        # removing any whiteSpaces
        s = s.strip()
        # sign var for + - signs
        sign = 1
        result = 0
        # if string is empty at start then return 0
        if not s :
            return 0
        
        # Determinig the sign 
        if s[0] == "-" or s[0] == "+" :
            if s[0] == "-" : sign = -1
            if s[0] == "+" : sign = 1
            s = s[1:]
            
        # Iterating through every charater in string, if it's a digit then set the value to the result var with * 10 to remove any leading zeros
        for char in s :
            if not char.isdigit() :
                break
            result = result * 10 + int(char)
        result *= sign
        
        # If the final result exceeds the 32-bit signed integer ranges, then it rounds it to the closest integer in the range
        if result < -2**31 : return -2**31 
        elif result > 2**31-1 : return 2**31-1

        return result;
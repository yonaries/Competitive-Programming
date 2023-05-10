class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(digit) for digit in str(a)]
        b = [int(digit) for digit in str(b)]
    
        # make sure the two binary numbers have the same length by padding zeros
        while len(a) < len(b):
            a.insert(0, 0)
        while len(b) < len(a):
            b.insert(0, 0)
    
        carry = 0
        result = []
    
        # loop through each digit in the two lists of integers
        for i in range(len(a)-1, -1, -1):
            
            # add the digits in the same column and the carry by XOR
            digit_sum = a[i] ^b[i] ^ carry
        
            # apply the AND operator to calculate the carry for the next column addition
            carry = (a[i] &b[i]) | (carry & (a[i] ^b[i]))
        
            # add the digit to the result list
            result.insert(0, str(digit_sum))
    
        # if there is a leftover carry, add it to the result list
        if carry == 1:
            result.insert(0, str(carry))
    
        # convert the result list back to a string and return it
        return ''.join(result)
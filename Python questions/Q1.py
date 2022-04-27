# *******************************************************************

def do_arithmetic(x, y, op = 'add'):
    '''
    The function takes three input arguments: a number x, a number y, and a string op representing an operation. The default operation is add.
    It does four arithmetic base on the two given numbers and returns the result.
    '''
    if op == '+' or op == 'add':
        return float(x + y)
    elif op == '-' or op == 'subtract':
        return float(x - y)
    elif op == '*' or op == 'multiply':
        return float(x * y)
    elif op == '/' or op == 'divide':
        if y == 0:
            print('Division by 0!')
            return None
        else:
            return float(x / y)
    else:
        print('Unknown operation')
        return None


def sum_of_digits(s):
    '''
    The function takes one input argument string s. 
    It calculates the sum of all the digits in the string and store the digits and non-digits values in two lists respectively.
    Finally, it prints 'the sum of digits operation performs' and 'the extracted non-digits', while return the sum of all the digits value.
    '''
    # Define a empty list for characters and numbers respectively. The 'b' is a blank string.
    chr = []
    num = []
    b = ''
    
    # Iterating the the given string, identify numbers or characters within it and place them to their list respectively.
    for i in s:
        if i.isdigit():
            num.append(i)
        else:
            chr += i
    
    # Iterating the number list, giving a '+' sign before each number.
    for i in num:
        b += '+' + i  # Now 'b' contains numbers and plus signs.
   
    # Do the sum of numbers calculation.
    total = sum([int(i) for i in num])

    # If there is no number in the input string but there are non-digits (characters):
    if len(num) == 0 and len(chr) != 0:
        print('The sum of digits operation could not detect a digit!')
        print('The extracted non-digits are', chr)
    # If given string is empty:
    elif s == '':
        print('Empty string entered!')
    # Apart from above 2 conditions:
    else:
        print('The sum of digits operation performs {}'.format(b[1:]))  # Ignoring the first plus sign in string 'b'.
        print('The extracted non-digits are', chr)
   
    return total

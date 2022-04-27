# CMT309 - 2021-2022 Coursework Q3
# Shang Li 21114121
# ************************************************************************************

import re

def function_renamer(code):
    '''
    The function takes one input argument string code.
    Then it finds the functions in the input code and rename them from underscore case to the camel case.
    Finally, it returns a dictionary and newcode.
    The dictionary contains hash code of the original function name, camel case version of original function name,
    and the caps version of original function name.
    The newcode is the code that successfully replaced the underscore case function from the original code by the camel case.
    '''
    # Defining the outputs.
    camelcase = []
    d = {}
    newcode = code

    # Finding all functions in the code.
    function = re.findall(r'def (\w+)', code)

    # Iterating functions, rename them to camel case and add them to a list sequentially, or keep them if there has no underscore in the function.
    for i in function:
        if re.findall(r'_',i) != []: 
            camel = re.sub(r'(?<=[a-zA-Z])_', ' ', i).title().replace(' ', '')
            camelcase.append(camel)
            # If there is underscore in the function.
            # Replacing the underscore (which after words) to space, then use title() to make the initial letter of words be uppercase.
            # Finally, replace the space with empty string, and add it to the camel case list.
        else:
            camelcase.append(i)
            # If there has no underscore in the function. Assuming the function is already in camel case, and add it to the camel case list directly.
         
    # Building a dictionary, functions are keys, its camel case are values.
    dict_funcam = dict(zip(function, camelcase))

    # Iterating all the function and place them in the dictionary with required format sequentially. 
    for i in function:
        d_temp = {i: {'hash': hash(i), 'camelcase': dict_funcam[i], 'allcaps': i.upper()}}
        d.update(d_temp)

    # Iterating the function list, replacing the original function name by camel case according to the paired dictionary (dict_funcam) respectively.
    # And then get the newcode, which function names are all in camel case.
    for i in function:
        newcode = newcode.replace(i, dict_funcam[i])
    
    return (d, newcode)

print(function_renamer('def Comeback'))
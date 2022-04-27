# ************************************************************************************

def pluralize(word):
    '''
    The function takes one input argument string word.
    Then it pluralizes the word and return a dictionary that contains plural of the word and its status.
    There are four statuses meaning:
    1) empty_string, it happens when the input word is an empty string.
    2) already_in_plural, it happens when the input word is already in plural.
    3) proper_noun, it happens when the input word is in the proper_nouns.txt file.
    4) success, it happens when the function successfully pluralized the input word.
    '''
    # Read the txt file, and turn the file into a list without '\n'
    f = open('proper_nouns.txt','r')
    a = f.readlines()
    s = [x.strip() for x in a]
    f.close()
    
    # Do not pluralize the word if the word follows these 3 conditions.
    if word == '':
        return {'plural':word, 'status':'empty_string'}
    elif word[-1] =='s':
        return {'plural':word, 'status':'already_in_plural'}
    elif str.lower(word) in s:
        return {'plural':word, 'status':'proper_noun'}
    
    # word ends with a vowel, add -s.
    elif word[-1] in ['a','e','i','o','u']: 
        return {'plural':word+'s', 'status':'success'}
   
    # word ends with 'y' and is preceded by a consonant (not in vowel), erase the last letter and add -ies.
    elif word[-1] == 'y' and word[-2:] not in ['ay','ey','iy','oy','uy']: 
        return {'plural':word[:-1] + 'ies', 'status':'success'}
    
    # word ends with 'f', erase the last letter and add -ves.
    elif word[-1]=='f':
        return {'plural':word[:-1] + 'ves', 'status':'success'}
    
    # word ends with 'sh'/'ch'/'z', add -es.
    elif word[-1]=='z' or word[-2:] in ['sh', 'ch']:
        return {'plural':word + 'es','status':'success'}
    
    # If none of the above applies, just add -s.
    else:
        return {'plural':word + 's','status':'success'}

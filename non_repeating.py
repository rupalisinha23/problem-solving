"""
return the first non repeating character from the given string
"""

def non_repeating(str1):
    char_count= {}
    for char in str1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] +=1
    for c in char_count:
        if char_count[c] == 1:
            return c
    return None

if __name__=='__main__':
    print(non_repeating('aabbc'))
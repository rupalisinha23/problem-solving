"""
return true if the two strings are one edit distance away.
"""

def is_one_away_same_length(str1, str2):
    count_diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count_diff +=1
        if count_diff > 1: return False
    return True


# Assuming that the second string is one character longer than the first one.
def is_one_away_diff_lengths(str1, str2):
    i = 0
    count_diff = 0
    while i < len(str2):
        if str1[i+count_diff] == str2[i]:
            i +=1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True


def is_one_away(str1, str2):
    if len(str1) - len(str2) >=2 or len(str2) - len(str1) >= 2:
        return False
    elif len(str1) == len(str2):
        return is_one_away_same_length(str1, str2)
    elif len(str1) > len(str2):
        return is_one_away_diff_lengths(str1, str2)
    else:
        return is_one_away_diff_lengths(str2, str1)

if __name__=='__main__':
    print(is_one_away('abcd','abacd'))
    print(is_one_away('abcd','abce'))
    print(is_one_away('abcd', 'abcdef'))




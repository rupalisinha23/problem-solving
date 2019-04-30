"""
given two arrays/lists A and B, return true if A is a rotation of B otherwise return false
"""

def is_rotation(A,B):
    if len(A) != len(B): return False

    key=A[0]
    indexB = -1

    for i in range(len(B)):
        if B[i] == key:
            indexB = i
            break
    if indexB == -1: return False

    for i in range(len(A)):
        j = (indexB + i)%len(A)
        if A[i] != B[j]:
            return False
    return True

if __name__=='__main__':
    print(is_rotation([1,2,3,4],[3,4,1,2]))



"""
Best time complexity: O(nlog(n))
Worse time complexity: O(nlog(n))
Space complexity: O(n)
"""


def mergeSort(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = mergeSort(x[:mid])
    z = mergeSort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


print(mergeSort([1,2,5,3,4]))
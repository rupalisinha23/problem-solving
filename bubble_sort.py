"""
Bubble Sort: settles the heavier elements at the end of the list first.
Worse case time complexity: o(n^2)
Best case time complexity: O(n)
Advantages: easier to understand, few lines of code, in-memory sorting, performs greatly when array is almost sorted.
Disadvantages: very expensive O(n^2)
"""

def bubble_sort(list1):
    for i in range(len(list1),0, -1):
        for j in range(0,i-1):
            noSwaps = True
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
                noSwaps = False
        if noSwaps:
            break

    return list1

print(bubble_sort([1,2,3,4,10,1]))
print(bubble_sort(([10,9,8,7,1])))
"""
Selection Sort
Time complexity: O(n^2)
Advantages: in-memory sorting, performs well on small lists, better than bubble sort only in the case of number of swaps
Disadvantages: Its time complexity is the main disadvantage.

"""

def selection_sort(list1):
    for i in range(len(list1)):
        lowest = i
        for j in range(i+1, len(list1)):
            if list1[j] < list1[lowest]:
                lowest = j

        if lowest != i:
            temp = list1[i]
            list1[i] = list1[lowest]
            list1[lowest] = temp
    return list1

print(selection_sort([3,1,5,10,2]))

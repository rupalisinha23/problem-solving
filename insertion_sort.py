"""
Worse Time complexity: O(n^2)
Best Time Complexity: O(n)

"""

def insertion_sort(list1):
    for i in range(1, len(list1)):

        # element to be compared
        current = list1[i]

        # comparing the current element with the sorted portion and swapping
        while i > 0 and list1[i - 1] > current:
            list1[i] = list1[i - 1]
            i = i - 1
        list1[i] = current


    return list1

print(insertion_sort([1,2,7,3,0]))
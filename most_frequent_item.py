"""
Find the most frequent item occuring in a list.
Below solution has O(n) time complexity.
"""

def most_frequent(given_array):
    max_count = -1
    max_item = None
    count={}

    for item in given_array:
        if item not in count:
            count[item] = 1
        else:
            count[item] +=1

        if count[item] > max_count:
            max_count = count[item]
            max_item = item

    return max_item

if __name__ == '__main__':
    given_array=[1,1,1,1,3,4,5,10,1, -1, -1, -1, -1, -1, -1, -1]
    print(most_frequent(given_array))

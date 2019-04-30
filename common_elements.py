"""
Given are the two sorted arrays/lists of unkown length. They can be empty even. We need to return the common elements.
Below solution has the time complexity of O(m+n) where m and n are the lengths of first and second array respectively.
"""

def common_items(list1, list2):
    p1,p2 = 0,0 # declare two pointers which
    result = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p2 +=1
            p1 +=1
        elif list1[p1] > list2[p2]:
            p2 +=1
        else:
            p1+=1
    return result

if __name__=='__main__':
    list1=[]
    list2=[]
    print(common_items(list1,list2))

    list1=[1,2,3,4]
    list2=[1,2,5,6]
    print(common_items(list1,list2))
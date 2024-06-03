def Insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j>= 0 and list[j] > key:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = key
    return list
list = [5, 2, 4, 6, 1, 3]
print(Insertion_sort(list))

#Time Complexity: O(n^2)
#Space Complexity: O(1)

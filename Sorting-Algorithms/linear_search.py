def Linear_search(list):
    for i in range(len(list)):
        if list[i] == i:
            return i
    return "NIL"
list = [1, 3, 2, 5, 6, 7]
print(Linear_search(list))

#Time Complexity: O(n)
#Space Complexity: O(1)

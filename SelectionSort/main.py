def selection_sort(array):
    n = len(array)

    for i in range(n-1):
        for j in range(i, n-1-i):
            print(array[i], array[j])


array = [5,1,4,2,8,9]
selection_sort(array)
print(array)
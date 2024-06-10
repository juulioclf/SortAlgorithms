def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_ind = i
        
        for j in range(i+1, n):
            if (array[j] < array[min_ind]):
                min_ind = j

        array[i], array[min_ind] = array[min_ind], array[i]
            

array = [5,1,4,2,8,9]
selection_sort(array)
print(array)
def bubble_sort(array):
    n = len(array)

    for i in range(n-1):
        print('i:', i)
        swapped = False

        for j in range(0, n-i-1):
            print('j:', j)

            if array[j] > array[j+1]: 
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]

        if not swapped:
            return



array = [5,1,4,2,8,9]
bubble_sort(array)
print(array)
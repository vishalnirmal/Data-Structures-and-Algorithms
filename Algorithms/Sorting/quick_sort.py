##############################################
# Quick Sort                                 #
# by Vishal Nirmal                           #
##############################################




def sort(arr, reverse=True):

    quick_sort(arr, 0, len(arr)-1, reverse)

def quick_sort(arr, low, high, reverse):

    if low<high:

        pivot = partition(arr, low, high, reverse)

        quick_sort(arr, low, pivot-1, reverse)

        quick_sort(arr, pivot+1, high, reverse)

def partition(arr, low, high, reverse):

    pivot = arr[high]

    i = low-1

    for j in range(low, high):

        if reverse:

            if arr[j] > pivot:

                i+=1

                arr[j], arr[i] = arr[i], arr[j]

        else:

            if arr[j] < pivot:

                i+=1

                arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1
#Quick Sort 

#Logic
def quick_sort(array_nums, left, right):
    #check
    if left < right:
        partition_position = partition(array_nums, left, right)
        #all elements that are less than the pivot element
        quick_sort(array_nums, left, partition_position - 1)
        #all elements that are greater then the pivot element
        quick_sort(array_nums, partition_position + 1, right)
        

def partition(array_nums, left, right)

#array
array_nums = [100, 7, 49, 1, 70, 36, 39, 69, 92, 48]
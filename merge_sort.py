#Merge Sort

#Logic
def merge_sort(array_nums):
    #check
    if len(array_nums) > 1: 
        #sub array - from beggining to the middle point
        left_arr_nums = array_nums[:len(array_nums)//2]
        #sub array - from the middle point to the end
        right_arr_nums = array_nums[len(array_nums)//2:]
        
#array
array_nums = [100, 7, 49, 1, 70, 36, 39, 69, 92, 48]
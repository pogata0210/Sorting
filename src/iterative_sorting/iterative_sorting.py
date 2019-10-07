# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        for j in range (cur_index, len(arr) ):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            
            # arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

       




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps_num = True
    while swaps_num:
        swaps_num = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # swap
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swaps_num = True
   
    
    
    
    
    
    return arr













# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


#initial commit





def binary_search(arr: int, num: int) -> int:
    
    first_indx = 0
    last_indx = len(arr)-1
    #print(f"first:{first_indx} last is:{last_indx}")
    
    while first_indx <= last_indx: #we need to know when to stop , and we will stop when last and first index the same = means we have only one arr[0]

    
        mid_indx = (first_indx + last_indx)//2 # we will get the middle
        
        if arr[mid_indx] == num:
            return mid_indx
        elif mid_indx == 0:
            return -1
        elif arr[mid_indx] > num:
            last_indx = mid_indx - 1
        elif arr[mid_indx] < num:
            first_indx = mid_indx + 1
            
                    
        
    return -1 #if number has not found

def binary_search_recursion(arr: list, num: int) -> int:
    
    mid_indx = len(arr)//2
    
    if arr[mid_indx] == num:
        return mid_indx
    elif mid_indx == 0:
        return -1
    
    elif arr[mid_indx] > num:
        return binary_search_recursion(arr[:mid_indx], num)
        
        
    elif arr[mid_indx] < num:    
        return binary_search_recursion(arr[mid_indx:], num)
        

    
    

if __name__ == "__main__":
    
    #binary search - for .Array should be sorted befor
    arr_list = [1, 21, 33, 44, 50, 61, 74, 86, 87, 98, 101, 110]
    #arr_list = [1, 21, 33, 50]
    
    #index_exist = binary_search(arr_list, 60) # return index if exist or -1 if not exist
    index_exist = binary_search(arr_list, 115)
    print(f"The index of the number is: {index_exist}")
    
    #method will just check if num exist or not exist in the list - can not return correct index - cause we are changinf array
    index_rec_exist = binary_search_recursion(arr_list, 33)
    print(f"The index of the number is: {index_rec_exist}")
    
    #try te recursive way but DO NOT recreate an array - save memmory way This implementation uses helper parameters (low, high) - which is more memory efficient.
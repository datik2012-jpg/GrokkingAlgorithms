#def hello():
    #print("Hello")
    
def quick_sort(arr: list):
    
    #two base when array is empty or arr with size 1 
    #if not arr:
        #return arr #noting to sort
    #if len(arr) == 1:
        #return arr  
    #the same base check which covers both base cases       
    if len(arr) < 2: 
        return arr
    #when arr size 2 
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
        else: #arr already sorted
            return arr
    #when size 3,4,5...and etc
    #need pick up pivot , we will pick up something in the middle of arr or first.I decided to pick up in the middle of arr
   
    pivot=len(arr)//2
    #print(f"pivot:{pivot}")
    #now need to put all values less then pivot in the left side and greater to the right side
    left_arr = []
    right_arr = []
    for i in range(0,len(arr)):
        #print(f"i{i}") #print index
        #print(f"value:{arr[i]}") # print value
        if arr[i] < arr[pivot] and i != pivot:
            left_arr.append(arr[i])
        elif arr[i] >= arr[pivot] and i != pivot:
            right_arr.append(arr[i]) 
    #when for completed we have in the lefts arr all values < arr[pivot] and in the right side all values > arr[pivot]         
    #add pivot to the end of left?
    # works fine with:: left_arr.append(arr[pivot])
    # works fine with: return quick_sort(left_arr) + quick_sort(right_arr)
    pivot_val = arr[pivot] # this is for creating on the fly pivot list with size 1: [pivot_val]
    #as well we can move pivot_val in before for lops and created comprehension "for"
    #left = [x for x in arr[1:] if x < pivot]
    #right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left_arr) + [pivot_val]  + quick_sort(right_arr)

if __name__ == "__main__":
    #hello()
    arr = [8, 5, 2, 10, 8, 6, 3, 4, 9, 1, 7, 1, 1] 
    #sorted_arr = quick_sort(arr)
    #arr = [9, 6, 8, 1, 6]
    sorted_arr = quick_sort(arr) 
    print(f"Sorted array: {sorted_arr}")   
    

def find_max(arr: list):
    
    if len(arr) == 1:
        return arr[0] # when array size ir only one - it is the max in this array
    elif not arr:
        return None  #when array is empty
        
    else: 
        
        tmp_max = find_max(arr[1:])
        
        if tmp_max > arr[0]:
            return tmp_max
        else: return arr[0]
    

def find_max2(arr: list):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else: return arr[1]
    else:
        sub_max = find_max2(arr[1:])
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max 



if __name__ == "__main__":
    array_list = [10, 5, 15, 20, 30, 100, 50, 70, 80, 90]
    minimal_list = [10,50,15,5]
    #for i in array_list:
        #print(i)
        
    #for i in range(len(array_list)):
        #print(array_list[i])   
        
    #found_max = find_max(minimal_list)
    #print(f"Found max value in the arrray list: {found_max}") 
          
    #option one      
    found_max = find_max(array_list)
    print(f"Found max value in the arrray list: {found_max}")   
    
    #option 2
    found_max = find_max2(array_list)
    print(f"Found max value in the arrray list: {found_max}")
      
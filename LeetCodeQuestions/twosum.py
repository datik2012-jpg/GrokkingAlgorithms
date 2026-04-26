




""" def sumtwo(arr:list, target: int) -> list:
    
    for x in arr:
        sub_sum = target - x   #
        first_index = arr.index(x)
        
        if sub_sum in arr and arr.index(sub_sum, first_index + 1):
            new_arr = []
            #new_arr.append(arr.index(x))
            #new_arr.append(arr.index(sub_sum))
            new_arr.extend([arr.index(x), arr.index(sub_sum)])
            return new_arr """
            


""" def sumtwo(arr:list, target: int) -> list:
    first_index = 1
    
    for x, v in enumerate(arr[first_index:]):
        sub_sum = target-v
        if sub_sum in arr:
            arr_index = []
            arr_index.append(arr.index(x))
            arr_index.append(arr.index(sub_sum))
            return arr_index
        else:
            first_index +=1 """

def sumtwo(arr:list, target: int) -> list:
    first_index = 0
    #second_index = 1
    while first_index +1 < len(arr):
        sub_sum = target - arr[first_index]
        try:
            second_index = arr.index(sub_sum, first_index + 1)
            arr_index = []
            arr_index.append(first_index)
            arr_index.append(second_index)
            return arr_index
        except ValueError:
            print("not found)")
            
        first_index += 1       
    
    #sub_sum = target - arr[first_index]
    #if first_index + 1 < len(arr) and sub_sum in arr[first_index:]:
        

if __name__ == "__main__":
    
    #given an array of integers and TARGET .Need return indexes of two integres in array which give the SUM exaclty as TARGET.Do not use the same number twice.
    #imput should have only one solution and not use the same element twice
    #arr = [2, 15, 11, 7] 
    #target = 9
    #output should be [0, 1] cause index 0 and 1 has target sum = 2 + 9 = target = 9 
    #arr = [3, 3]
    #target = 6
    
    arr = [3, 2, 4]
    target = 6
    
    index_arr = sumtwo(arr, target)
    print(index_arr)
    
    
    
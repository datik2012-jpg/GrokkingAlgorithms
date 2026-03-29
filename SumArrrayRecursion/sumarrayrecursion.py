def hello():
    print("Hello, World!")
    
    
def sum_array(arr: list):
   if not arr:
       return 0  
   else:
       return arr[0] + sum_array(arr[1:])
   
   
   
def sum_array2(arr: list):
   if not arr:
       return 0  
   else:
       first_val = arr.pop(0)
       
       return first_val + sum_array2(arr)  


if __name__ == "__main__":
    hello()
    
    #option 1
    sum_array = sum_array([1, 2, 3, 4, 5, 6])
    print(f"The sum of the array is: {sum_array}") 
    
    #option 2 with pop
    sum_array2 = sum_array2([1, 2, 3, 4, 5, 6, 7])
    print(f"The sum of the array2 is: {sum_array2}")
    

#given an array of integers and TARGET .Need return indexes of two integres in array which give the SUM exaclty as TARGET.Do not use the same number twice.
#imput should have only one solution and not use the same element twice .So if tagret is 4 you can not take twice index 0 like in: [2,3]
#arr = [2, 15, 11, 7] 
#target = 9
#output should be [0, 1] cause index 0 and 1 has target sum = 2 + 9 = target = 9 
#arr = [3, 3]
#target = 6
    
def sumoftwo(arr: list , target: int) -> list:
   #the tricky thing we will check if target-num already part of the dictionary if not will add it with index , if exist return the index.In this way we will not have found already added num.
   dict = {}
   index_1 = 0
   final_arr_indexes = []
   for num in arr:
       tmp_val = target - num
       if tmp_val in dict:
           #get the index and we can return both indexes
           index_2 = dict[tmp_val]
           final_arr_indexes.append(index_1)
           final_arr_indexes.append(index_2)
           return final_arr_indexes
       else:
           dict[num]= index_1
       index_1 += 1    
           
       



if __name__ == "__main__":
    #print("Hello")
    
    #i can try solution when i use the distionary - the solution is tricky we check the target-num exist in the dict if not we add key=num val=index
    
    #arr = [3, 2, 4]
    #target = 6
    
    #arr = [2, 15, 11, 7] 
    #target = 9
    
    arr = [3, 3]
    target = 6
    
    solution = sumoftwo(arr, target)
    print(solution)
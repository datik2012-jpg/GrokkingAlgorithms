




def findnotexistinginarray(nums: list) -> list:
   new_nums = []
   for x in range(1, len(nums)+1):
       #print(x)
       if x not in nums:
           new_nums.append(x)
           
   return new_nums        

    











if __name__ == "__main__":
    
    #given a array numns of n integers  where nums[i] is a range [1,n] 
    #returns an array of all integers in the range [1,n] that do not appear in nums
    #example imput [4,3,2,7,8,2,3,1]
    #output: [5,6]
    
    #Note as you can see numps.len=8 so all the numbers from 1 to 8 should exist in array what is not exist add to the new_arr
    nums = [4, 3, 2, 7, 8, 2, 3, 1]  #so 4 and 5 are not existing .nums.len = 7
    print(f"Nums length is: {len(nums)}")
    
    new_arr = findnotexistinginarray(nums)
    print(new_arr)
    
    nums2 = [1, 1]
    new_arr = findnotexistinginarray(nums2)
    print(new_arr)
    
    
    nums3 = [1, 2, 3, 1]
    new_arr = findnotexistinginarray(nums3)
    print(new_arr)
    
    
    
    
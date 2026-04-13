





#dict solution
def check_duplicate(nums: list) -> bool:
    dict = {}
    
    for num in nums:
        #print(num)
        if num in dict:
            return True
        else:
            dict[num] = num
        
    return False    


    #set solution
def check_duplicate_set(nums: list) -> bool:
    new_set=set(nums) #make from list a set which will remove duplicates
    for x in new_set:
        print(x)
     
    #simple check
    if len(new_set) != len(nums):
        return True    
    return False    





if __name__ == "__main__":
    #given an integer list,return True if any value appers at least twice
    nums = [1, 2, 3, 1]
    #nums = [1, 2, 3, 4]
    #nums = [1, 1, 1, 1, 2, 3, 3, 3, 1]
    
    #use dict capabilities
    print(f"answer is: {check_duplicate(nums)}")
    
    #thisset = {"apple", "banana", "cherry", "apple"} #will not add second time an apple , cause it is exit
    #print(thisset.pop()) #will remove random element (sets are working in this way)
    
    #use sets capabilities
    print(f"Used set to check the answer: {check_duplicate_set(nums)}")
    
    
    
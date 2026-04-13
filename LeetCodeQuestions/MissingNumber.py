

def check_missing(nums: list, n: int)-> int:
    
    #numbers in the list already so we can check if it exist or not
    for x in range(0,n+1):
        if x not in nums:
            return x

#use sum to find no existing - but if there will be some number  like 1000 it can not work [0, 1000] n=2
def check_missing_2(nums: list, n: int)-> int:
    return sum(range(0, n+1)) - sum(nums) #




if __name__ == "__main__":
    #given an list of nums
    #contains n distinct numbers in a range [0, n]
    #return only the number in the range which is missing
    
    #Example: nums = [3, 0, 1]
    Output : 2 
    #Exmpl: n=3 so in range [0,3] - there all the numbers in a range 0 , 1 , 2
    
    for x in range(0,3):
        print(x)
        
    nums = [3, 0, 1]
    n=3
    print(f"Find missing number: {check_missing(nums, n)}")    
    
    
    nums = [0, 1]
    n=2
    print(f"Find missing number: {check_missing(nums, n)}")  
    
    
    #try something different - to sum the numbers
    
    nums = [3, 0, 1]
    n=3
    print(f"Find missing number: {check_missing_2(nums, n)}") 
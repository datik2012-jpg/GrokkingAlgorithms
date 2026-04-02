
#only find MAX 'C' substring in the string
def findsubstring(s: str):
    #for i in s:
        #print(i)
    #print(s[0])
    count_max = 0
    count = 0
    for index in range(0,len(s)-1):
        if s[index] == "C":
            #print("hello")
            if s[index-1]  == "C":
                count+=1
            else:
                count=1
        if count_max < count:
            count_max=count
    return count_max 


def findsubstring2(s: str):
    max = ''
    max_c = ''
    for i in s:
        if i == 'C':
            max_c +='C' #creation our substring
            if len(max_c) > len(max):
                max=max_c
        else:
            max_c='' #when at least one in subtring not 'C' we will destroy our max_c to be empty again         
        
    #print(f"Max substrint is max_c:{max}")
    return max    

def subreplace(s: str):
    s = s.replace('A',' ').replace('B', ' ')
    print(s)
    print(s.split(' ')) #will creaete a list like this: ['CCCC','','CC','','','']
    mx = max(s.split(' '), key=len)
    
    print(mx,len(mx))

#find any MAX substring in the string                      
def findanysubstring(s: str):
    #for i in s:
        #print(i)
    #print(s[0])
    count_max = 0
    count = 0
    for index in range(1,len(s)-1): #will start from 1 cause we dont want to fail index-1 int the first iteraction
        if s[index] == s[index-1]:
            count+=1
        else:
            count=1
        if count_max < count:
            count_max=count
    return count_max 



if __name__ == "__main__":
    #find max substring
    s ='CCCBACCBCCCCCACCABCACCACCCCAAABAABBBCCCCBCCCCBBBCBCBACCACCABCACCBBBBCACBCCCCCAC'
    
    #this method will find MAX substring for letter 'C' only 
    sub_str = findsubstring(s)
    print(f"Found max C substring: {sub_str}")
    
    #another way to find MAX 'C' substring
    sub_str2 = findsubstring2(s)
    print(f"Found max C substring2: {sub_str2} which is: {len(sub_str2)}")
    
    #use replace
    subreplace(s)
    
    #find any MAX substring
    any_sub_string = findanysubstring(s)
    print(f"Found max ANY substring: {any_sub_string}")
from collections import deque


class Node:
    
    def __init__(self, char, value):
        self.char = char
        self.value= value
        self.right = None
        self.left = None
    


def countCharInSentence(text: str):
    print(text)
    dict = {}
    for mychar in text:
        if mychar in dict: #we check if char as a key exist in the dictionary - to decide if to add it (if not existing when first time) - if exsit count++
            counter = dict[mychar]
            counter +=1
            dict[mychar] = counter
        else: #when first time we meet a char
            dict[mychar]=1    
    
    return dict


def sortDictByValues(char_dict):
    #will do python 3.7 feature - sort dict (ascending) by values 
    sorted_dict= dict(sorted(char_dict.items(), key=lambda x: x[1]))
    return sorted_dict

        
        
        
def createQueueNodesFromСharDict(char_dict):
    #need sort the chars by value - i will do the binary sort
    node_deque = deque()
    print(len(char_dict))
    for key, val in char_dict.items():
       node = Node(key, char_dict[key])
       print(f"{node} and {key}") 
       node_deque.append(node)
       
    return node_deque     
    




if __name__ == "__main__":
    
    #Huffman Algorithm : https://habr.com/en/articles/144200/
    
    text_for_zip = "beep boop beer!"
    
    #create a dictionary - where char is a key and value is how many time char exist in the sentence
    
    char_dict = countCharInSentence(text_for_zip)
    print(f"Dict of char and values:{char_dict}")
    
    #we need to sort a dict by values - from Python 3.7 we do have this option - so will implement
    sorted_dict = sortDictByValues(char_dict)
    print(f"Sorted by values dict:{sorted_dict}")
    
    #create a queue where Node  (char,value) with The minimum value will be added to the queue first  (left in the will be min value and we will as well pop from the left only)
    #i think this it's  good time to create Node object which will include char and it's value instead the dictionary
    node_queue = createQueueNodesFromСharDict(sorted_dict)
    print(node_queue) #will print the queue adresses
    
    #proceed next week !!!!
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
    

def CreateHuffmanTree(node_queue):
    #print Value by index
    #print(f"Print by index:{node_queue[0].char,node_queue[0].value}") # (r,1)
    
    #extract two first min values from the queue.Connect them to the Node ,add this new Node back to the queue in correct order (might be need additional temp queue for helping)
    print(f"Queue length :{len(node_queue)}")
    root = "" #node which going to be a root and we need return it
    while len(node_queue)>1: #let's leave this logic at the moment - we leave one last Node in the queue
        
        left_1 = node_queue.popleft()
        left_2 = node_queue.popleft()
        
        node = Node("", left_1.value + left_2.value)   #new Node will have empty char and value = sum of sub Nodes
        node.left = left_1
        node.right = left_2
        
        #add the node to correct place in the queue 
        #to do this we need temp queue - to keep extracted values
        temp_queue = deque()
        #find the correct index where to add the new Node
        index_to_add = -1 #in case if we have found new largest node ,then we can just add it to the end
        for i in range(0, len(node_queue)):
            #print(f"hey:{i}")
            if node.value <= node_queue[i].value:
                index_to_add=i
                break
        #add to the correct index
        added_node_flag=0
        if index_to_add == 0:
            node_queue.appendleft(node) # when our new Node value is less then first Node value in the queue so add it just to the left side of the queue
            added_node_flag=1
        if index_to_add == -1: #just add to the end of the queue
            node_queue.append(node)
            added_node_flag=1
        
        else: #when index>0 it means we need extact to the temp queue all Nodes which < than our new Node
            while index_to_add > 0:
                temp_queue.append(node_queue.popleft()) # we exctractinfg and adding this Node to the temp
                index_to_add -= 1
            #adding our node to the queue cause we extact all < than our node
            if added_node_flag == 0:
                node_queue.appendleft(node)
                
            while len(temp_queue) > 0: #now need to add back all Nodes which we extracted before
                tmp=temp_queue.pop() #extract from the right end of the queue where we have BIGEST tmp number
                node_queue.appendleft(tmp) #add to the left end of the queye - to keep the order
                     
        root = node_queue
        print(f"index found:{index_to_add}")
    
    return root 
        
    #for i in range(0, len(node_queue)-1): # cause we need one less pair then the size
        #extract two from the left
        #left_1 = node_queue.popleft()
        #left_2 = node_queue.popleft()
        #print(f"{left_1.char} {left_2.char}")

if __name__ == "__main__":
    
    #Huffman Algorithm : https://habr.com/en/articles/144200/
    
    text_for_zip = "beep boop beer!"
    #text_for_zip = "abc"
    #text_for_zip = "abbcccc" # has a vug returns 10
    #text_for_zip = "abbccc"
    
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
    
    #now in node_queue we have Nodes added in the order Node(r,3),Node(!,1),Node(p,2) and etc
    #next step is start to group two MIN Nodes together to one Node and add it back to the QUEUE in the correct by order place
    #new Node will have the sum of two childrens - char we can leave as empty and we can understand this is
    #method will create for us final tree
    Root = CreateHuffmanTree(node_queue)
    print("Dani")
    #proceed from here - for path creation
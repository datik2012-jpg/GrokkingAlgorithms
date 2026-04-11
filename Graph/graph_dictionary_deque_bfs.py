from collections import deque

#just playing with deque
deque_X = deque()
deque_X.append('Dani')
deque_X.append('Alex')
deque_X.append('Sonya')
deque_X.append('Sanya')
deque_X.append('Zusu')


print(deque_X.popleft()) 
print(deque_X.popleft())

print(deque_X.pop()) #remove from the right side (for action like stack)

print(deque_X[1]) 

#grokking algorithms - graph in dictionary: check who is the oranges seller - someone who has 'm' in the end of the name :-)

graph = {}
graph["Me"] = ["Alice", "Bob", "Kler"]
graph["Bob"] = ["Anuj", "Peggi"]
graph["Alice"] = ["Peggi"]
graph["Kler"] = ["Tom", "Jhonny"]
graph["Anuj"] = []
graph["Peggi"] = []
graph["Tom"] = []
graph["Jhonny"] = []


#graph_deque = deque()
#graph_deque+=graph["Me"]
#print(graph_deque)
#print(graph_deque.popleft())

def check_if_seller(graph_deque):
    #for option
    #for i in range(0, len(graph_deque)):
        #person = graph_deque.popleft()
        #print(person)
    while graph_deque:
        person = graph_deque.popleft()
        print(person)
        #check if seller: someone who has 'm' in the end of the name :-)
        if person[-1] == 'm':
            print("Found oranges seller")
            return person
        #as well valid check
        #if person.endswith("m"):
            #print("Ends with m - so found a seller")   
    return None         
                    
        

def find_orange_seller(graph):
    graph_deque = deque()
    for key, val in graph.items():
        #print(key, val)
        #print(graph[key])
        graph_deque += graph[key] #add from the list to the deque
        checkedName=check_if_seller(graph_deque)
        if checkedName != None:
            return checkedName
    return None

def check_seller(person):
    if person[-1] == "m":
        return person
    else:
        return None

def check_the_tree_for_seller(new_deque, graph):
    already_checked_name = [] # we do not want get a loop when some person is friend for another and opponent (infinity lop can happen) so we will check if the name already been checked and do not check twice
    
    while new_deque: #run until our deque has something
        person = new_deque.popleft() # extart only from the left side
        checked_seller_name = check_seller(person)
        if checked_seller_name != None:
            return checked_seller_name #so we have found a seller !!!!! WOW WOW WOW
        else:
            #check if person not been checked before - to escape from infinity loop
            if person not in already_checked_name:
                already_checked_name.append(person)
                new_deque+=graph[person] # when the name is not seller we will add all his connections(friends) to the deque
            else:
                print(f"Name already exist in the list:{person}")    
    return None #if orange seller has not found in all the tree !!!       

if __name__ == "__main__":
    #in this way we are searching with looping in the dictionary - which is not correct (see second solution)
    found_seller=find_orange_seller(graph)
    if found_seller != None:
        print(f"Found seller: {found_seller}")
    else:
        print("Not found oranges seller")
        
        
    #add to the deque the name from the name - so it will be like connection of friends
    #we will start from the first Key in the dictionary and proceed:
    #similar to BFS search 
    first_key = list(graph.keys())[0]
    print(first_key)
    
    #create deque
    new_deque = deque()
    new_deque+=graph[first_key] # we added to the deque only the first connection
    print(new_deque)
    
    seller = check_the_tree_for_seller(new_deque, graph)
    if seller != None:
        print(f"Amazing: We have found the oranges seller:{seller}")
        
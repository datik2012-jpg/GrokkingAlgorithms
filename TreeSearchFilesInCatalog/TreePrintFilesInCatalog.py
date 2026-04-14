
import os
import sys
sys.stdout.reconfigure(encoding='utf-8') #need this cause without it will fail to print HEBROW files with an error: UnicodeEncodeError: 'charmap' codec can't encode characters

from pathlib import Path
from collections import deque



#code will do BFS alghoritm for a TREE of folders and print all files in the folder.Folder will be added to the deque. 
def bfs_tree_print_file_names(root):
    print("Print all files in directory and sub directory - use TREE BFS alhoritm")
    search_deque = deque()
    search_deque.append(root)
    while search_deque: # until we have folders in the deque
         folder= search_deque.popleft()
         #print(folder)
         for item in folder.iterdir():
            #print(item)
            if item.is_dir():
                #print(f"folder:{item}")
                search_deque.append(item) #add tp the deque if item is directory (aka folder)
            elif item.is_file(): #if item is file
                print(item)
                    
    




if __name__ == "__main__":
    
    #just to print all files in specific path
    #files = os.listdir("C:/Users/User/Downloads")
    
    #for file in files:
        #print(f"Found a file: {file}")   
        
    #for example we want to print all files in all folders - like to search in TREE and alghoritm BFS  
    #I have created a folders (D:\TreeNode)  so we can run and check the code 
    
    
    root = Path("D:/TreeNode") #create oject WindowsPath from the string path
    print(root)
    print(root.exists())  
    print(root.is_dir())
    
    for item in root.iterdir(): #this for will prim folders and files in the current TreeNode folder
        print(f"{item}")
        
    print("")    
     
    #run over folder and all subfolders and find files and print path to them - TREE BFS alghoritm .Solution has Not inlcuded shorcuts or link folders which can create a LOOP in the tree.
    bfs_tree_print_file_names(root)  
    
    #if item.is_symlink(): #Check if the item is a symbolic link
        #print("This is a symbolic link") 
        
    #Check if the item is a Windows .lnk shortcut
    #if item.suffix.lower() == ".lnk":
        #print("This is a Windows shortcut (.lnk)") 
        
    #Note:
    #is_symlink() detects real filesystem links, not .lnk files.

    #Windows .lnk files are not symlinks — they are regular files that contain metadata.

    #If you want, I can show you how to resolve a .lnk file to the real target (requires pylnk3 or winshell).       
    
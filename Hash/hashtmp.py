
import hashlib

def hash_func():
    print(hash(10))
    print(hash(20))
    print(hash(3.10))
    
    print(hash("dani"))
    print(hash((1, 2, 3)))
    
    cortage = (1, 2, 3, 4, 5)
    print(cortage[1])
    
    text = "dani"
    #sha256
    hash_object = hashlib.sha256(text.encode())
    print(hash_object)
    hex_diget = hash_object.hexdigest()
    print(f"hex:{hex_diget}")
    
    # Использование MD5 (небезопасно для криптографических целей!)
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    print(f"md5:{md5_hash}") # 32 символа
    
    
    #sha1
    sha1_object = hashlib.sha1(text.encode())
    print(sha1_object)
    hex_sha1_object = sha1_object.hexdigest()
    print(f"sha1:{hex_sha1_object}")


def hash_some_text_5mb():
    data = b"Hello world!"
    h = hashlib.sha256()
    
    #read text each time by 5mb and add to the sha256 : SHA256("Hello" + " worl" + "d!") = final sha
    for i in range(0, len(data), 5):
        chunk = data[i:i+5]
        print("Chunk:", chunk)
        h.update(chunk)

    print("Hash:", h.hexdigest())
    
    
def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as file:
        while chunk := file.read(1024):
            h.update(chunk)
    return h.hexdigest()   


def play_dict():
    my_dict = {}
    
    my_dict['dani'] = "liv"
    my_dict['alex'] = 'livs'
    
    print(my_dict)

if __name__ == "__main__": #read : https://sky.pro/wiki/python/heshirovanie-v-python-osnovnye-metody-i-primery/
    hash_func()
    
    #if even obne byte in the text will be changed - hash function will be changed - so not the same as before .Good for validation changes
    hash_some_text_5mb()
    
    #in case we  want to validate a files , example read by chunks 1028mb and create a hash
    
    #hash_file(need to provide some file)
    
    play_dict()
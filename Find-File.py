import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

val = input("Please enter the name of your file :") #format like s.txt
val2 = input("Please enter path that you want to search :") #format like C:\
path = find_all(val, val2)
if not path:
    print("There is no such file in this path!") 
else: print("Here is your file :" , path )

import os

def cleanCluster(file,num,type="txt",prefix="file"):
    newName = prefix+num+"."+type
    os.rename(file,newName)

location = input("Enter the location of Directory/Folder : ")
file_type = input("Enter the type of file : ")
prefix_name = input("Enter the prefix : ")

num = 0       # Rename by numbers
os.chdir(location)    # Give the directory which you want to clean
for i in os.listdir():
    num+=1
    cleanCluster(i,str(num),file_type,prefix_name)

print(os.listdir()) # Printing renamed files
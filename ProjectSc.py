import os

def Encrypt(file_name, key):
    file = open(file_name, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(file_name, key):
    file = open(file_name, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    
choice=1
while(choice!=4):
    print("1.Create a file\n2.Encrypt an existing file\n3.Decrypt an Existing File\n4.Quit")
    choice=int(input("Enter a choice: "))
    if(choice==1):
        save_path=os.getcwd()
        file_name=input("Enter filename with .txt extension: ")
        filename=os.path.join(save_path,file_name)
        str=input("Enter data to be saved: ")
        f1=open(filename,"w")
        f1.write(str) 
        f1.close()
    #num=int(input("1.Encrypt\n2.Decrypt\n3.Quit"))
    if(choice==2):
        key=int(input("Enter a key between 1-255: "))
        filename=input("\nEnter filename with extension: ")
        Encrypt(filename,key)
        print("File Encrypted!\nThe Encrypted filename is: ")
        print("CC-"+filename)
        os.remove(filename)
        continue
    if(choice==3):
        key=int(input("Enter the key given for encryption: "))
        filename=input("\nEnter encrypted filename with extension: ")
        Decrypt(filename,key)
        print("File Decrypted!\nThe Decrypted filename is: ")
        print(filename)
        continue
    
    
        
        
        

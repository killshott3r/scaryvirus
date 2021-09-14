import os
import shutil

select = input("Do you want to delete a FILE or a FOLDER?")

if 'file' in select.lower():
    location = input(r"Please copy and paste the location of the file [EXAMPLE: C:\Users\User\Desktop\Visual Basic 6]: ")
    file = input(r"Please copy and paste the name of the file (Use less important files) [EXAMPLE= test.txt]: ")

    path1 = os.path.join(location + "\\" + file)
    print(path1)
    input("Close the program if you messed up the file path now itself. [enter space if you are sure]: ")

    os.remove(path1)
    print("YOUR VERY IMPORTANT FILE HAS BEEN DELETED!!! :O")
    input('')
elif 'folder' in select.lower():
    folder = input(r"Please copy and paste the folder you want to delete. [EXAMPLE: C:\Users\User\Desktop\Visual Basic 6]: ")
    input("Close the program if you messed up the file path now itself. [enter space if you are sure]: ")

    shutil.rmtree(folder)
    print("YOUR VERY IMPORTANT FOLDER HAS BEEN DELETED!!! :O")
    input('')
else:
    print("please input one of the options.")
    input('')
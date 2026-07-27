### Read a Whole File

with open ('./SampleFiles/example.txt','r') as file:
    file_content = file.read()
    #print(file_content)

# Read File Line By Line
with open ('./SampleFiles/example.txt','r') as fileLine:
    for line in fileLine:
        #print(line)  # has a newline charachter at the end of each line
        print(line.strip()) # remove new line character

# Writing a file (Overwriting)
with open ('./SampleFiles/writeExample.txt','w') as filewrite:
    filewrite.write('Hello World\n')
    filewrite.write('this is a sample writing into a file\n ')

# Writing a file (Append to the file not Overwriting)
with open ('./SampleFiles/writeExample.txt','a') as filewrite:
    filewrite.write('This line is appended to the file \n')


# write list of lines to a file
lines = ['First line \n','Second line \n','Third line\n','Forth Line\n']
with open ('./SampleFiles/writeExample.txt','a') as filewrite:
    filewrite.writelines(lines)

# Binary Files Writing
data = b'\x00\x01\x02\x03\x04'
with open ('./SampleFiles/BinaryFileExample.txt','wb') as Bfilewrite:
    Bfilewrite.write(data)

# Binary Files Reading
with open ('./SampleFiles/BinaryFileExample.txt','rb') as BfileRead:
    binarycontent = BfileRead.read()
    print(binarycontent)

# Create new Directory
import os
newdir = 'SampleFiles/packages'
if os.path.exists(newdir):
    print(f'The Folder  {newdir} is Exist')
else:
    os.mkdir(newdir)
    print(f'Directory "{newdir}" is Created')

# Listing Files And Directories
items = os.listdir('.')
print("\n",items)

# Create a file Full Path
dir_name = 'SampleFiles'
file_name ='example.txt'
full_path = os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)

# Exception handling allowes you to handle errors and take correct action without stopping the running program
a: int = 5
try:
    b= int(input("Engter an Interger number:  "))
    result = a/b
    #a = c
except ZeroDivisionError as ex:  # catch devision by zero
    print(ex)
    print('Please enter the dominator greater than 0')
except Exception as ex1:  # catch other events
    print(ex1)
else:
    print(f"\nThe Result is {result} ")
finally:
    print("Execution is comleted...")
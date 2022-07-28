#This code will read all file name in active directory or any specific directory. It will ask for user inout and if user inout matches with text file content then output 
# would be printed.
# os.getcwd() = used to get the current working directory 
# glob.glob() = returns a list of files which matches pattern 
#Re module is for pattern/expresion match 


import os, glob ,re 


word = re.compile(r'[A-Za-z,\.]+')
while True:
    user_input = input("enter text to match")
    for filename in glob.glob('*.txt'):
        with open(os.path.join(os.getcwd(),filename),'r')as f:
         text =f.read()
         textFinder = word.findall(text)
         for i in textFinder:
            if user_input == i:
                print(user_input)
        print(filename)
        print(text)  

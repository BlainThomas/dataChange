import os
import json

def change_text():
    for file in sourcepath:
        inputfile = 'to-be-replaced/'+ file
        print('updating' + inputfile)
        with open(inputfile, 'r') as inputfile:
            filedata = inputfile.read()
            freq = 0
            freq = filedata.count(texttofind)
        destinationpath = 'replaced/' + file
        filedata = filedata.replace(texttofind,texttoreplace)
        with open(destinationpath, 'w') as file:
            file.write(filedata)
            print('just %d finished' %freq)

texttofind = input("What do you want to get ride of? ")
texttoreplace = input("What do you want to replace it with?") 
sourcepath = os.listdir('json/')

change_text()


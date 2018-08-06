from urllib.request import urlopen
import pickle
import os 
import glob

nothing = '90052'


# while True:
    # with open('6_/'+nothing+'.txt') as f:
        # text = f.read()
    # print(text)
    # nothing = text[16:]
    
    
    
for file in glob.glob('6_/*.txt'):
    with open(file) as f:
        text = f.read()
    print(text)
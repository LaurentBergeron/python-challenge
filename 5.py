from urllib.request import urlopen
import pickle

url = urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()

data = pickle.loads(url)

for row in data:
    string = ''
    for char, num in row:
        string += char*num
    print(string)
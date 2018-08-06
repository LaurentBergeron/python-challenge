from urllib.request import urlopen

# next_nothing = 12345
next_nothing = 8022

while True:
    url = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(next_nothing))
    nothing = url.read().decode('utf-8')
    print(nothing)
    try:
        index = nothing.find('and the next nothing is ') 
        next_nothing = int(nothing[index+24:index+29])
    except:
        break


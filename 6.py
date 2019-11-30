import zipfile

nothing = '90052'

zf = zipfile.ZipFile('6_.zip')
total_str = ''

while True:
    fname = nothing+'.txt'
    try:
        with open('6_/'+fname) as f:
            text = f.read()
    except:
        break
    print(text)
    total_str += zf.getinfo(fname).comment.decode("utf-8") 
    nothing = text[16:]

print(total_str)
    
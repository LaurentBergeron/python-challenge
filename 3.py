with open('3_.txt') as file:
    text = file.read()
    
# text = 'asdasdTTTyTTTasdkjsbadbYYYiOOOt'

text_caps_filter = ''.join(['A' if x.isupper() else 'a' if x.islower() else '_' for x in text])

start = 0
while True:
    index = text_caps_filter.find('aAAAaAAAa', start)
    if index==-1: 
        print('break')
        break
    start =index+1
    print(text[index+4])
    

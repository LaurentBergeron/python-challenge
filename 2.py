with open('2_.txt') as file:
    text = file.read()
    
rare_counts = [chr(x) for x in range(256) if text.count(chr(x)) == 1]

result = ''.join([char for char in text if char in rare_counts])

print(result)
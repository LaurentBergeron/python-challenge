import matplotlib.pyplot as plt
import numpy as np
import re
plt.ioff()
im = plt.imread('7_.png')

# # Plot full image
# plt.figure()
# plt.imshow(im)
# plt.show()


# # Plot grey scale along x
# plt.figure()
# plt.plot(im[46,:,0]*255)
# plt.show()

# Convert grey scale to int
code = (im[46,:,0]*255).astype(int)
# Remove excess pixels (take one every 7 pixels)
code = code[range(0,len(code),7)]
# Decode from ASCII
answer = ''
for x in code:
    answer += chr(x)
print(answer)

# Print answer
splitted_answer = re.findall('\[(.+)\]', answer)[0].split(', ')

for num in splitted_answer:
    print(chr(int(num)), end='')
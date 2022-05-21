import keyGen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('picture1.bmp')

#plt.imshow(img)
#plt.show()

#generating chaotic keys
height = img.shape[0]
width = img.shape[1]

key = kg.keyGen(0.01, 3.95, height*width)

print(key)

#encryption substitution with XOR

z = 0
enimg = np.zeros(shape =[height, width,4], dtype = np.uint8)
for i in range(height):
    for j in range(width):
        #pixel value is XORed with key
        enimg[i,j] = int(img[i,j])^key[z]
        z += 1

#print(enimg)

#plt.imshow(enimg)
#plt.show()
#plt.imsave('EncryptedImage.bmp',enimg)

# #decryption

z = 0
decimg = np.zeros(shape = [height, width, 4],dtype = np.uint8)  #third parameter (4 here) defiens the number of chanels required for the image. for an RGB its 3 and thirs alpha stands for transparency
for i in range(height):
    for j in range(width):
        #pixel value is XORred with key
        decimg[i, j] = enimg[i,j]^key[z]
        z += 1

plt.imshow(decimg)
plt.imsave('Decrypted_image.bmp', decimg)
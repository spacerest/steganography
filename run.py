import matplotlib.pyplot as plt
from steg import *
from PIL import Image

img1 = Image.open('./test/test3.jpg')
img2 = Image.open('./test/test4.jpg')
img_array_1 = np.asarray(img1, dtype="uint8")
#print(img_array_1)
img_array_2 = np.asarray(img2, dtype="uint8")
#print(img_array_2)
result_img_array = combine_image_arrays(img_array_1, img_array_2)
#print(result_img_array)
plt.imshow(result_img_array.astype('uint8'))
#im = Image.fromarray(result_img_array.astype(np.uint8))
#im.save("./test/result3.jpg")




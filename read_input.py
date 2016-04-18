from skimage.io import imread
import numpy as np
#
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
im = np.asarray(imread("chars74k-lite/chars74k-lite/a/a_0.jpg"))
#
'''for row in im:
	print(row)'''
#
test_data=[]
test_solutions=[]
for i in range(450):

#
#indices = np.dstack(np.indices(im.shape[:2]))
#data = np.concatenate((im, indices), axis=-1)
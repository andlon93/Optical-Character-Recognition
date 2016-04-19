"""
================================
Recognizing hand-written digits
================================

An example showing how the scikit-learn can be used to recognize images of
hand-written digits.

This example is commented in the
:ref:`tutorial section of the user manual <introduction>`.

"""

def readImage(filename):
	train_data = []
	image = imread(filename)
	img = np.asarray(image)
	img.setflags(write=True)
	thresh = threshold_otsu(img)
	binary = image > thresh
	binary = np.reshape(binary,(1,400))
	train_data.append(np.asarray(binary[0]).astype(float))
	return train_data

from skimage.filters import threshold_otsu
from skimage.io import imread
from sklearn import svm
import numpy as np
import read_input as ri
import matplotlib.pyplot as plt
import math


#Read 5 "A"'s and 5 "B"s
train_set, train_ans, test_set, test_ans = ri.read_input_otsu_OLE()


images_and_labels = list(zip(test_set, test_ans))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    arr_ind = 0
    c = -1
    t_img = []
    tt_img = []
    for i in range (400):
    	if c ==19:
    		arr_ind += 1
    		c = 0
    		t_img.append((tt_img))
    		tt_img = []
    	else:
    		c+=1
    	tt_img.append((image[i]))
    plt.imshow(t_img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('')


clf = svm.SVC()
#print (len(train_set[0]))

clf.fit(train_set, train_ans)

predicted = clf.predict(test_set)
count = 0
for i in range(len(predicted)):
	print ("Pred, Fasit: ", predicted[i],test_ans[i])
	if (predicted[i] == test_ans[i]):
		count += 1
print ("% correct: ",(count/len(predicted))*100)

images_and_predictions = list(zip(test_set[4:], predicted))
u = 0
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
	plt.subplot(2, 4, index + 5)
	plt.axis('off')

	arr_ind = 0
	c = -1
	t_img = []
	tt_img = []
	for i in range (400):
		if c ==19:
			arr_ind += 1
			c = 0
			t_img.append((tt_img))
			tt_img = []
		else:
			c+=1
		tt_img.append((image[i]))

	plt.imshow(t_img, cmap=plt.cm.gray_r, interpolation='nearest')
	plt.title('')
	u+=1
print("Interwebs")

print ("Input: 'BFromInterWeb2'. Prediction:",predict("BFromInterWeb2.jpg"))
print ("Input: 'QFromInterWeb2'. Prediction:"',predict("QFrominterweb2.jpg"))

plt.show()


from skimage.io import imread
import numpy as np
#
def kd_reduce(func,seq):
    res = seq[0]
    for item in seq[1:]:
        res = func(res,item)
    return res
def flatten_image(image_array):
    def flatten(a,b): return a + b
    return kd_reduce(flatten, image_array.tolist())
#
#print(flatten_image(imread("chars74k-lite/chars74k-lite/"+"a"+"/"+"a"+"_"+"0"+".jpg")))
def read_input():
	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	#alphabet=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,19,20,21,2]
	n=70
	train_data=[]
	train_solutions=[]
	for i in range(n):
		for letter in alphabet:
			train_data.append(np.asarray(flatten_image(imread("chars74k-lite/chars74k-lite/"+letter+"/"+letter+"_"+str(i)+".jpg"))))
			train_solutions.append(ord(letter))
	#
	m=88
	test_data=[]
	test_solutions=[]
	for i in range(n,m):
		for letter in alphabet:
			test_data.append(np.asarray(flatten_image(imread("chars74k-lite/chars74k-lite/"+letter+"/"+letter+"_"+str(i)+".jpg"))))
			test_solutions.append(ord(letter))
	#
	print(len(train_data))
	print(len(train_solutions))
	print(len(test_data))
	print(len(test_solutions))
	return train_data, train_solutions, test_data, test_solutions
if __name__ == '__main__':
	a,b,c,d=read_input()
	print(len(a[0]))
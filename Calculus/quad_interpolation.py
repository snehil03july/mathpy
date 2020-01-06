#This is a function which reads data of points from a file and plots the quadratic interpolation of the points.
#Function should be called in the following format: quad_interpolation('xyz.csv',N) 
# where N is the number of interpolated points between two input data points

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

style.use('dark_background')

def quad_interpolation(file_name,N):

	x,y = np.loadtxt(file_name, unpack=True, delimiter = ',')

	list1 = []
	list2 = []
	print(len(x))
	print(len(y))

	for i in range(len(x)-1):

		for j in range(0,N):

			list1.append(x[i] + j*((x[i + 1] - x[i])/N))

	#list1.pop()				
	v = 1.0

	for j in range(len(x)-2):

		for k in range(len(list1)):

			if(x[j] <= list1[k] <x[j + 1]):
		
				list2.append(((list1[k]-x[j+1])*(list1[k]-x[j+2])*y[j])/((x[j]-x[j+1])*(x[j]-x[j+2])) + ((list1[k]-x[j])*(list1[k]-x[j+2])*y[j+1])/((x[j+1]-x[j])*(x[j+1]-x[j+2])) + ((list1[k]-x[j])*(list1[k]-x[j+1])*y[j+2])/((x[j+2]-x[j])*(x[j+2]-x[j+1])))	

	while(len(list1)>len(list2)):
		list1.pop()
	while(len(list2)>len(list1)):
		list2.pop()	
	print(len(list2))
	print(len(list1))
	plt.plot(x,y,label='Linear interpolated points',color='r')

	plt.scatter(x,y,label='Input points',color='g')

	plt.plot(list1,list2,marker='x',color='y',label='Quadratic interpolated points')

	plt.ylabel('Y-AXIS')
	plt.xlabel('X-AXIS')
	plt.legend(loc='best')

	plt.title('Linear Interpolation')

	plt.show()
  
#quad_interpolation('graph.csv',7)	





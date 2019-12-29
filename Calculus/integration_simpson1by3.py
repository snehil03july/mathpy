'''To integrate any user defined function f, or any other function in NumPy, call:
int_simpson(function, lower_limit, upper_limit, num_of_intervals_of_integration)
'''
import numpy as np
def int_simpson(f,a,b,N):
	w=(b-a)/N
	area=(w/3)*(f(a)+f(b))
	i=a
	for i in range(1,N):
		if i%2==0:
			area+=(w/3)*2*f(a+i*w)
		else:
			area+=(w/3)*4*f(a+i*w)
	return area

#print(int_simpson(np.sin,0,(np.pi)/2,100))



 

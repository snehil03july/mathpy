#This function gives the approximate derivative of a user defined function or any function from Numpy at a point x = a
#Call the function as follows: derivative(function, a, Number step size) example:print(derivative(np.sin,np.pi,0.00001))
#Number step size (h) should tend to zero for a better approximate 

import numpy as np

def derivative(f,a,h):

	return (f(a + h) - f(a - h))/(2*h)



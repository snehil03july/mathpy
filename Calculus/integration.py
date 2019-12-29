#This function gives the approximate integral of a user defined function or any function from Numpy from x = a to x = b with N divisions.
#Call the function in the following way: trap_integral(function,lower_limit,upper_limit,No.of_Intervals_of_integration)

def trap_integral(f,a,b,N):

	w = (b - a)/N

	c = 0

	for i in range(N):

		c += f(a + i*w) + f(a + (i + 1)*w)

	return(c*0.5*w)	

#print (trap_integral(np.sin,0,2*(np.pi),10000))

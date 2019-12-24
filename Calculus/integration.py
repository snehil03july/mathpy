#This function gives the approximate integral of a "function available in numpy" from x = a to x = b with N divisions.
#Input the function as np.yourfunction in the function trap_integral

def trap_integral(f,a,b,N):

	w = (b - a)/N

	c = 0

	for i in range(N):

		c += f(a + i*w) + f(a + (i + 1)*w)

	return(c*0.5*w)	

#print (trap_integral(np.sin,0,2*(np.pi),10000))

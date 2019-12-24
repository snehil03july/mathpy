# Enter the coefficients of the two lines in the standard form ax+by+c = 0
#This function returns the coordinates of the point of intersection of two lines in the form of a tuple

def solve_2var(a1,b1,c1,a2,b2,c2):

	if(a1*b2 - a2*b1 == 0 and c1/c2 != a1/a2):
		print(f"The two lines {a1}x+{b1}y+{c1} = 0 and {a2}x+{b2}y+{c2} = 0 are parallel and they don't intersect") 

	elif(a1*b2 - a2*b1 == 0 and c1/c2==a1/a2):

		print(f"The two lines {a1}x+{b1}y+{c1} = 0 and {a2}x+{b2}y+{c2} = 0 coincide")
			

	else:	

		x = (b1*c2 - b2*c1)/(a1*b2 - a2*b1)

		y = (a2*c1 - a1*c2)/(a1*b2 - a2*b1)

		if(y == -0.0):

			y = 0.0

		if(x == -0.0):

			x = 0.0	

		return(x,y)

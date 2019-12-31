#The function line_eq(x1,y1,x2,y2) will give the equation of line passing through (x1,y1) and (x2,y2)


def P(l0, l1):

	x = 'x'

	x = x.replace(x[0], f'y = {l0}x - {l1}')

	y = x.split('x')
	

	if(y[1] == f'--{-l1}'):

		x = x[0].replace(x[0], f'y = {l0}x + {-l1}',1)

	if(l0 == 1.0):

		x = x[0].replace(x[0], f'y = x + {-l1}',1)

	if(l0 == -1.0):
	
		x = x[0].replace(x[0], f'y = -x + {-l1}',1)

	if(l0 == 0.0):
	
		x = x[0].replace(x[0], f'y = {-l1}',1)	

	if(l1 == 0.0 or l1 == -0.0):

		x = x[0].replace(x[0], f'y = {l0}x')		

	return(x)




def line_eq(x0,y0,x1,y1):


	p = []

	p.append([x0,y0])
	p.append([x1,y1])
	

	for i in range(len(p)):

		for j in range(2):

			p[i][j] = float(p[i][j])	

	
		
	l0 = (p[0][1] - p[1][1])/(p[0][0] - p[1][0])

	l1 = (p[1][0]*p[0][1] - p[0][0]*p[1][1])/(p[0][0] - p[1][0])

	a = P(l0, l1)

	print(a)


line_eq(0,2,3,5)	


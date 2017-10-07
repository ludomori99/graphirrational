from math import *
import matplotlib.pyplot as plt


               # OPEN
root_number = 'pi'
cifre = 10000000
quanti = 1000


file_name = str(root_number)+'.txt'
file = open(file_name, "rb").read()



def discalculator(initial, precision, x, y):

	numeri = file[initial:precision]
	index2 = 0
	for val in numeri:
		if index2 % 4 == 0:
			x += int(val)	
		if index2 % 4 == 2:
			x -= int(val)
		if index2 % 4 == 1:
			y += int(val)
		if index2 % 4 == 3:
			y -= int(val)
		index2 += 1
	distance = sqrt(x**2 + y**2)
	return distance, x, y  

	
				# Loop + Graph 
xes = []
yes = []
xval = 0
yval = 0
for i in range (1,quanti+1):
	precision = (cifre/quanti)*i
	initial = (cifre/quanti)*(i-1)
	values = discalculator(initial, precision, xval, yval)
	xes.append(precision)
	yes.append(values[0])
	print(precision, values[0])
	xval = values[1]
	yval = values[2]
plt.plot(xes, yes)
plt.show()

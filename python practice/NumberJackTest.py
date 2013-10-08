import sys
from Numberjack import *

def main(argv):
	filename = argv[0];
	f = open(filename,"r")
	dimensions = f.readline().split(" ")
	boxwidth = dimensions[0]
	boxheight = dimensions[1]
	
	n = boxwidth
	m = boxheight
	matrix = Matrix(n*m,n*m,1,9)

	model = Model()
"""
for row in matrix.row
	model.add(AllDiff(row)	

for column in matrix.column
	model.add(AllDiff(column))
"""
print matrix

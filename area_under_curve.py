#Collaborative Assignment 2
#Eric and Marcus

import numpy as np

def line_area(intervals,x1,x2):
  m=3
  b=2
  area  = 0
  base = (x2-x1)/intervals
  for i in range(1,intervals+1):
    x = base*(i-.5)
    height = m*x+ b 
    area  = height*base + area
  integral = .5*m*(x2**2-x1**2)+b*(x2-x1)
  return area, integral

def parabola_area(intervals, x1, x2):
  a = 1
  b=2
  c=-2
  area = 0
  base = (x2-x1)/intervals
  for i in range(1,intervals+1):
    x = base*(i-.5)
    height = a*(x**2) + b*x + c
    area  = height*base + area
  integral = 0 #need to calculte exact integral value
  return area, integral 

def complicated_area(intervals,x1,x2):
	a = 1	
	m = 3
	b = 2
	area = 0
	base = (x2-x1)/intervals
	for i in range(1,intervals+1):
		height = (a*base*(i-.5) + b)*(ma.e)**(-c*base*(i-.5)) #for y=x
		area  = height*base + area
	integral = -(ma.e)**(-c*x2)(a+b*c+a*c*x2)/c**2+(ma.e)**(-c*x1)(a+b*c+a*c*x1)/c**2
	return area, integral


intervals = int(input("Enter the number of rectangles to use:"))

x1=0
x2=5
rectangle_line_area, integral_line = line_area(intervals,x1,x2)
rectangle_parabola_area, integral_parabola = parabola_area(intervals,x1,x2)



#do some sort of loop to estimate area with a variety for the number of rectangles for each of the 3 functions
#in (x,y) 2D array, keep appending the values of (n, E(n)) where E(n) is the error for a given number of rectangles
#then plot each function

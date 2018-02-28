#Collaborative Assignment 2
#Eric and Marcus

import numpy as np
import math as ma

def line_area(intervals,x1,x2):
  m=3
  b=2
  area  = 0
  base = (x2-x1)/intervals
  for i in range(1,intervals+1):
    x = base*(i-0.5)
    height = m*x+ b 
    area  = height*base + area
  integral = .5*m*(x2**2-x1**2)+b*(x2-x1)
  return area, integral

def parabola_area(intervals, x1, x2):
  a = 1.0
  b=2.0
  c=-2.0
  area = 0
  base = (x2-x1)/intervals
  for i in range(1,intervals+1):
    x = base*(i-0.5)
    height = a*(x**2) + b*x + c
    area  = height*base + area
  integral = (a/3.0)*(x2**3-x1**3) + (b/2.0)*(x2**2-x1**2) + c*(x2-x1)
  return area, integral 

def exp_area(intervals,x1,x2):
	a = 1	
	m = 3
	b = 2
	c=3
	area = 0
	base = (x2-x1)/intervals
	for i in range(1,intervals+1):
	  x=base*(i-0.5)
	  height = (a*x + b)*(ma.exp(-c*x))
	  area  = height*base + area
	integral = -ma.exp(-c*x2)*(a+b*c+a*c*x2)/c**2+ma.exp(-c*x1)*(a+b*c+a*c*x1)/c**2
	return area, integral


#intervals = int(input("Enter the number of rectangles to use:"))

x1=0
x2=10
i=1
rectangle_line_area, integral_line = line_area(i,x1,x2)
rectangle_parabola_area, integral_parabola = parabola_area(i,x1,x2)
rectangle_exp_area, integral_exp = exp_area(i,x1,x2)

line_difference = ma.fabs((rectangle_line_area-integral_line)/integral_line)*100
parabola_difference = ma.fabs((rectangle_parabola_area-integral_parabola)/integral_parabola)*100
exp_difference = ma.fabs((rectangle_exp_area-integral_exp)/integral_exp)*100

n=np.array([i])
line_error = np.array([line_difference])
parabola_error = np.array([parabola_difference])
exp_error = np.array([exp_difference])

print line_area(11,x1,x2)[0]

while i < 10:
  i += 1
  rectangle_line_area, integral_line = line_area(i,x1,x2) #"""rectangle_parabola_area, integral_parabola = """
  rectangle_parabola_area, integral_parabola = parabola_area(i,x1,x2)
  rectangle_exp_area, integral_exp = exp_area(i,x1,x2)
  line_difference = ma.fabs((rectangle_line_area-integral_line)/integral_line)*100
  parabola_difference = ma.fabs((rectangle_parabola_area-integral_parabola)/integral_parabola)*100
  exp_difference = ma.fabs((rectangle_exp_area - integral_exp)/integral_exp)*100
  
  n = np.append(n,i)
  line_error = np.append(line_error,line_difference)
  parabola_error = np.append(parabola_error,parabola_difference)
  exp_error = np.append(exp_error,exp_difference)
  

print parabola_error
#do some sort of loop to estimate area with a variety for the number of rectangles for each of the 3 functions
#in (x,y) 2D array, keep appending the values of (n, E(n)) where E(n) is the error for a given number of rectangles
#then plot each function

#Collaborative Assignment 2
#Eric and Marcus

import numpy as np
import math as ma
import matplotlib as mpl
import matplotlib.pyplot as plot

def line_area(intervals,x1,x2):
  m=3.0
  b=2.0
  area  = 0.0
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
	  x=base*(i-.5)
	  height = (a*x + b)*(ma.exp(-c*x))
	  area  = height*base + area
	integral = -ma.exp(-c*x2)*(a+b*c+a*c*x2)/c**2+ma.exp(-c*x1)*(a+b*c+a*c*x1)/c**2
	return area, integral


#intervals = int(input("Enter the number of rectangles to use:"))

x1=0.0
x2=5.0
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

#Calculate Areas, Integrals and then Errors for each function for n from 1 to given number. 
while i < 100:
  i += 1
  rectangle_line_area, integral_line = line_area(i,x1,x2)
  rectangle_parabola_area, integral_parabola = parabola_area(i,x1,x2)
  rectangle_exp_area, integral_exp = exp_area(i,x1,x2)
  line_difference = ma.fabs((rectangle_line_area-integral_line)/integral_line)*100
  parabola_difference = ma.fabs((rectangle_parabola_area-integral_parabola)/integral_parabola)*100
  exp_difference = ma.fabs((rectangle_exp_area-integral_exp)/integral_exp)*100
  n = np.append(n,i)
  line_error = np.append(line_error,line_difference)
  parabola_error = np.append(parabola_error,parabola_difference)
  exp_error = np.append(exp_error,exp_difference)

#Plot the Error in the estimate as a function of each type of function

plot.figure()
plot.title("Error in Riemann Sum Estimate for a Line")
plot.scatter(n,line_error)
plot.show()

plot.figure()
plot.title("Error in Riemann Sum Estimate for a Quadratic Function")
plot.scatter(n,parabola_error)
plot.show()


plot.figure()
plot.title("Error in Riemann Sum Estimate for a Exponential Function")
plot.scatter(n,exp_error)
plot.show()
  #need to fix issue with computer rounding error for linear plot since it is perfect estimate everytime (get values for error on order of 10^(-13)

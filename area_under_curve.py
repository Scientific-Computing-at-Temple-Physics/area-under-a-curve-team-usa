#Collaborative Assignment 2
#Eric and Marcus

import numpy as np

def line_area(intervals,x1,x2):
  m=3
  b=2
  area  = 0
  base = (x2-x1)/intervals
  for i in range(1,intervals+1):
    height = base*(i-.5)*m + b #for y=x
    area  = height*base + area
  integral = .5*m*(x2**2-x1**2)+b*(x2-x1)
  return area, integral




intervals = int(input("Enter the number of rectangles to use:"))

x1=0
x2=5
rectangle_area, integral = line_area(intervals,x1,x2)

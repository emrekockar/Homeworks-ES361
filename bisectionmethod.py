#BISECTION METHOD FOR ES361 NUMERICAL METHODS#

import math

equation = input()
error_margin = float(input())
lower_boundary = float(input())
upper_boundary = float(input()) 
def f(x):
  return eval(equation)
f(lower_boundary)
f(upper_boundary)
previous_intermediate = 0
i = 0
while True: 
  i = i+1 
  if f(lower_boundary)*f(upper_boundary) < 0:
    intermediate = ((lower_boundary)+(upper_boundary))/2
    #print("Iteration ", i , "[",lower_boundary,",",upper_boundary,"]")
    print(f"Iteration {i} [{lower_boundary} , {upper_boundary}]")
    if i > 1:
      error = abs(((intermediate - previous_intermediate) / intermediate))
      if error <= error_margin:
        #print("Root is found at iteration"  , i  , intermediate)
        print('\x1b[6;37;42m' , "Root is found at iteration"  , i  , intermediate , '\x1b[0m')
        break  
    if f(intermediate)*f(lower_boundary) < 0:
      upper_boundary = intermediate
      previous_intermediate = intermediate
    else:
      lower_boundary = intermediate
      previous_intermediate = intermediate
  else:
    print("Poor Estimation")

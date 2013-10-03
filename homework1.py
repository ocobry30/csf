# Name: Joshua Kendall
# Evergreen Login: kenjos03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a1 = 1
b1 = -5.86
c1 = 8.5408

x1 = (-b1 + math.sqrt(b1**2 - 4 * a1 * c1)) / (2 * a1)  
x2 = (-b1 - math.sqrt(b1**2 - 4 * a1 * c1)) / (2 * a1)

print "x =", x1,",", x2 

###
### Problem 2
###

print "Problem 2 solution follows:"

from hw1_test import a, b, c, d, e, f

print a,"\n", b,"\n", c,"\n", d,"\n", e, "\n", f


###
### Problem 3
###

print "Problem 3 solution follows:"

ans3 = ((a and b) or (not c) and not (d or e or f))
print ans3

###
### Collaboration
###

# Bryan O'Connor, Gabriel Cangas

###
### Problem 4
###

print "Problem 4 solution follows:"


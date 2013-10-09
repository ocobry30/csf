# Name: Joshua Kendall
# Evergreen Login: kenjos03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"
from hw2_test import n

i = 0
sum = 0

while(i <= n):
    sum = sum + i
    i = i + 1 
    
print sum



###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

denom = 2.0
decRep = 0.0

while(denom < 11):
    decRep = 1 / denom
    print decRep
    denom = denom + 1

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range (0, n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
factorial = 1

for i in range (1, n+1):
    factorial = factorial * i
    
print n,"! =", factorial    

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"


numlines = 10


for i in range (0, numlines):
    factorial = 1
    n = numlines - i
    for j in range (1, n + 1):
        factorial = factorial * j
        
    print factorial

    
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
    
n = 10
ln = 0.0

for i in range (1, n + 1):
    factorial = 1.0
    for j in range (1, i + 1):
        factorial = factorial * j
        
    ln = ln + (1 / factorial)
    
ln = ln + 1

print ln

#no collaborators, no outside references besides python references




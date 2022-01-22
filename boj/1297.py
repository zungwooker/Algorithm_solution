import math

diag, height, width = map(int, input().split())
x = math.pow((diag*diag)/((height*height+width*width)), 1/2)
print(int(x*height), int(x*width))
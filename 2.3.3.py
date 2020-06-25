from math import sqrt

diamStr=input("Enter the length of the diameter:   ")

diameter=int(diamStr)

chordStr = input( " Enter the chord length:          ")
chord = int(chordStr)


radius = (diameter/2)

s = sqrt (diameter**2+chord**2)

h = (s/2-radius)

i= (2/3*chord*h)

j=(h**3/2*chord)

area = (i+j)

print (area)
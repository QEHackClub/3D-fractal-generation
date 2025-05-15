import sympy as sym


"""
#make equilateral
use maths not sympy
"""



#initial .stl file
name=input("give your creation a name\n")
f=open("C:/Users/euanr/3D Objects/"+ name + ".stl", "w")
mod=int(input("mod value:\n"))
f.write("solid " + name + "\n")

import numpy as np

def squareflatz(x,y,z,length):
    #a function to create a square with given length from the given coords as bottom left
    p1 = np.array([float(x),float(y),float(z)])
    p2 = np.array([float(x),float(y+length),float(z)])
    p3 = np.array([float(x+((length/86.60254038)*100)),float(y),float(z)])
    N = np.cross(p2-p1, p3-p1)
    f.write("facet normal "+ str(N[0])+" "+str(N[1])+" "+str(N[2])+"\n")
    f.write("outer loop\n")
    f.write("vertex " + str(x) +" "+ str(y)+" " + str(z)+"\n")
    f.write("vertex " + str(x) +" "+str(y+length)+" "+str(z)+"\n")
    f.write("vertex " + str(x+((length/86.60254038)*100)) + " "+str(y) +" "+str(z)+"\n")
    f.write("endloop\n")
    f.write("endfacet\n")
    p1 = np.array([float(x+((length/86.60254038)*100)),float(y+length),float(z)])
    p2 = np.array([float(x),float(y+length),float(z)])
    p3 = np.array([float(x+((length/86.60254038)*100)),float(y),float(z)])
    N = np.cross(p2-p1, p3-p1)
    f.write("facet normal "+ str(N[0])+" " + str(N[1])+" "+str(N[2])+"\n")
    f.write("outer loop\n")
    f.write("vertex " + str(x+((length/86.60254038)*100)) +" "+ str(y+length)+" " + str(z)+"\n")
    f.write("vertex " + str(x) +" "+str(y+length)+" "+str(z)+"\n")
    f.write("vertex " + str(x+((length/86.60254038)*100)) + " "+str(y) +" "+str(z)+"\n")
    f.write("endloop\n")
    f.write("endfacet\n")
def squareflaty(x,y,z,length):
    p1 = np.array([float(x+((length/86.60254038)*100)),float(y),float(z+length)])
    p2 = np.array([float(x+((length/86.60254038)*100)),float(y),float(z)])
    p3 = np.array([float(x),float(y),float(z)])
    N = np.cross(p2-p1, p3-p1)
    f.write("facet normal "+str(N[0])+" "+str(N[1])+" "+str(N[2])+"\n")
    f.write("outer loop\n")
    f.write("vertex " + str(x+((length/86.60254038)*100)) +" "+ str(y)+" " + str(z+length)+"\n")
    f.write("vertex " +str(x+((length/86.60254038)*100))+" "+str(y)+ " "+str(z)+"\n")
    f.write("vertex " +str(x)+" "+str(y)+" "+str(z)+"\n")
    f.write("endloop\n")
    f.write("endfacet\n")
    p1 = np.array([float(x+((length/86.60254038)*100)),float(y),float(z+length)])
    p2 = np.array([float(x),float(y),float(z+length)])
    p3 = np.array([float(x),float(y),float(z)])
    N = np.cross(p2-p1, p3-p1)
    f.write("facet normal "+ str(N[0])+" "+str(N[1])+" "+str(N[2])+"\n")
    f.write("outer loop\n")
    f.write("vertex " +str(x+((length/86.60254038)*100))+" "+str(y)+" "+str(z+length)+"\n")
    f.write("vertex " +str(x)+" "+str(y)+" "+str(z+length)+"\n")
    f.write("vertex " +str(x)+" "+str(y)+" "+str(z)+"\n")
    f.write("endloop\n")
    f.write("endfacet\n")
def squareflatx(x,y,z,length):
    p1 = np.array([float(x),float(y+length),float(z+length)])
    p2 = np.array([float(x),float(y+length),float(z)])
    p3 = np.array([float(x),float(y),float(z)])
    N = np.cross(p2-p1, p3-p1)
    f.write("facet normal "+ str(N[0])+" "+str(N[1])+" "+str(N[2])+"\n")
    f.write("outer loop\n")
    f.write("vertex " + str(x) +" "+ str(y+length)+" " + str(z+length)+"\n")
    f.write("vertex " +str(x)+" "+str(y+length)+ " "+str(z)+"\n")
    f.write("vertex " +str(x)+" "+str(y)+" "+str(z)+"\n")
    f.write("endloop\n")
    f.write("endfacet\n")
    p1 = np.array([float(x),float(y+length),float(z+length)])
    p2 = np.array([float(x),float(y),float(z+length)])
    p3 = np.array([float(x),float(y),float(z)])
    N = np.cross(p2-p1, p3-p1)
    f.write("facet normal "+ str(N[0])+" "+str(N[1])+" "+str(N[2])+"\n")
    f.write("outer loop\n")
    f.write("vertex " +str(x)+" "+str(y+length)+" "+str(z+length)+"\n")
    f.write("vertex " +str(x)+" "+str(y)+" "+str(z+length)+"\n")
    f.write("vertex " +str(x)+" "+str(y)+" "+str(z)+"\n")
    f.write("endloop\n")
    f.write("endfacet\n")
def cube(x,z,y,length):
    squareflatz(x,y,z,length)
    squareflatz(x,y,z+length,length)
    squareflaty(x,y,z,length)
    squareflaty(x,y+length,z,length)
    squareflatx(x,y,z,length)
    squareflatx(x+((length/86.60254038)*100),y,z,length)

#how many layers of the pyramid
#length=2.703
length=2.708
#.125
layers=int(input("how many layers: \n"))
baseH=86.60254038/layers
print("making progress estimates \n")
n=0
total=0

for x in range(1,layers+1):
    n=n+x
    total=total+n
percentages=[round(total/20),round(total/10),round((total/10)*1.5),round(total/5),round(total/4),round((total/10)*3),round(total/100*35),round(total/100*40),round(total/100*45),round(total/2),round(total/100*55),round(total/100*60),round(total/100*65),round(total/100*70),round(total/100*75),round(total/100*80),round(total/100*85),round(total/100*90),round(total/100*95),round(total)]
print("calculating and creating the file ()")
rep="false"
done="false"
print(percentages)
lower=24
for layer in range(lower,layers):
    zs=[]#clear values in the slice
    #treat abc as algebraic unknown variables
    a = sym.Symbol('a')
    b = sym.Symbol('b')
    c = sym.Symbol('c')
    #use a+b+c raised to the layer as a calculation for pascals pyramid
    x="+ " + str(sym.expand((a+b+c)**layer))
    #take the bases of the result and store as the numbers in pascals pyramid
    for y in range(len(x)):
        numbers=["0","1","2","3","4","5","6","7","8","9"]
        if layer==lower and rep =="false":
            zs.append(int(1))
            rep="True"
            calculated=1
        elif x[y]=="+" and x[y+2] not in numbers:
            z=1
            zs.append(int(z))
            calculated=calculated+1
        elif x[y]=="+":
            d=y
            z=""
            while x[d+2] in numbers:
                z=z+x[d+2]
                d=d+1
            zs.append(int(z))
            calculated=calculated+1
        try:
            if percentages.index(round(calculated)) != done:
                position=percentages.index(round(calculated))
                print((position+1)*5,"% done")
                done=position
        except ValueError:
            done="false"
        
            #add these to a list of values on this slice
    #print the slice
    #print(len(zs))
    #print(layer, end='       ')
    for var in range(len(zs)):
        #sort through the slice and determine what to shade via below mod
        if  zs[var]%mod==1:
            abc=0
            cba=0
            while var> cba or var == cba:
                abc=abc+1
                cba = cba + abc
                if var<cba or var == cba:
                    row=abc
                    z=(abc-(layer-layers)*0.5)                    
                    posinline=var-cba
                    x=float((abc/2)-posinline)-((layer-layers)*0.5)
                    y=float(((layers-layer+length)*3.125)/100)*86.60254038
                    x=(x+(layers-z)+length)*3.125
                    z=float(((z+length)*3.125)/100)*86.60254038
                   #float((x+(layers-z)+length)*3.125),float(z+length)*3.125
            #we want to shade this number, so the y value is the slices - the slice that it is on and the z value is the row that it is on in that slice
            cube(x,y,z,length)
#finish and close our 3d file
print("done")
f.write("endsolid "+name)
f.close()

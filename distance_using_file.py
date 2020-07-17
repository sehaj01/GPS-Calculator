from tkinter import *
from math import *
#------------------------------------------------
def EquiRectDist(la1,lo1,la2,lo2):
    '''
    Compute distance between 2 points with Equirectangular approximation
    this approximation is approporiate for small distances'
    longitude and latitude are supposed to be in radian
    '''
    R=6371*(10**3)
    x=(lo2-lo1)*cos((la1+la2)/2)
    y=la2-la1
    d=sqrt(pow(x,2)+pow(y,2))*R
    return d

def EquiRectDistDeg(la1,lo1,la2,lo2):
    return(EquiRectDist(radians(la1),radians(lo1),radians(la2),radians(lo2)))
def calculate():
    Fname=e1.get()
    F=open(Fname,"r")
    L=[]
    a=[[],[]]
    t=[]
    result=0
    F.readline()
    for l in F.readlines():
        L=l.split(";")
        a[0].append((L[0]))
        a[1].append((L[1]))
        t.append(float(L[-1]))
    #LL=[Lat,Long]    
    #print(L[1][1])
    #print(LL[1][1])
    for i in range(1,len(a[0])-1):
        a=float(a[0][i])
        b=float(a[1][i])
        c=float(a[0][i+1])
        d=float(a[1][i+1])
        result=result+EquiRectDistDeg(a,b,c,d)
    V.set(str(result))               
    F.close

#------------------------------------------------
#    Main Program
#------------------------------------------------
window=Tk()
window.title("Distance using file")

l1=Label(window,text="File name:")
l1.grid(row=0,column=0)
e1=Entry(window,bg="pink")
e1.grid(row=0,column=1)

l2=Label(window,text="Distance:")
l2.grid(row=1,column=0)


l3=Label(window,text="Time:")
l3.grid(row=2,column=0)

l4=Label(window,text="Speed:")
l4.grid(row=3,column=0)

V=StringVar()
l5=Label(window,textvariable=V)
l5.grid(row=1,column=1)

S=StringVar()
l6=Label(window,textvariable=S)
l6.grid(row=2,column=1)

W=StringVar()
l7=Label(window,textvariable=W)
l7.grid(row=3,column=1)

l8=Label(window,text="m")
l8.grid(row=1,column=2)

l9=Label(window,text="s")
l9.grid(row=2,column=2)

l10=Label(window,text="m/s")
l10.grid(row=3,column=2)

b1=Button(window,text="Quit",command=quit)
b1.grid(row=4,column=0)

b2=Button(window,text="Calculate",command=calculate)
b2.grid(row=4,column=2)


window.mainloop()

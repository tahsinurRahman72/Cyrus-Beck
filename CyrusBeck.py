import numpy as np
import math as m

#Calculate D:
def D(x_0,y_0,x_1,y_1):
    x_D=(x_1-x_0)
    y_D=(y_1-y_0)
    D=[x_D,y_D]
    return D

def NiD(func):
    N=[(-1,0),(0,1),(1,0),(0,-1)] #[left, top, right, bottom]
    ND=[] #[left, top, right, bottom]
    for i in range(0,len(N)):
        ND.append(np.dot(N[i],func))

    return ND


# P=(x_0,y_0)+(np.dot(t,D))
def calculateT(i):
    if(i==0):
        return round((-(x_0-x_min)/(x_1-x_0)),8) # t_left(x_0,x_1,x_min)

    elif(i==1):
        return round((-(x_0-x_max)/(x_1-x_0)),8) #t_right(x_0,x_1,x_max):

    elif(i==2):
        return round((-(y_0-y_max)/(y_1-y_0)),8) #t_top(y_0,y_1,y_max):

    elif(i==3):
        return round((-(y_0-y_min)/(y_1-y_0)),8) #t_bottom(y_0,y_1,y_min):


def P(x_0, y_0, t, func):
    D=func
    tdotD=np.dot(t,D)
    p=np.sum([[x_0,y_0],tdotD],axis=0)
    return p


def cyrusBeck(x_0,y_0,x_1,y_1):
    lineSegment=[[x_0,y_0],[x_1,y_1]]
    N=[(-1,0),(0,1),(1,0),(0,-1)]
    c=0
    tEntering=[] #[left, top, right, bottom]
    tLeaving=[] #[left, top, right, bottom]
    d=D(x_0,y_0,x_1,y_1)
    NdotD=[] #[left, top, right, bottom]
    NdotPoints=[]
    t=[]
    P1=[x_1,y_1]
    P0=[x_0,y_0]
    P0_new=[]
    P1_new=[]
    
    if(P1==P0):
        print("lol")
    else:
        t_Enter=0
        t_Leave=1       
        NdotD=NiD(d)
        for i in range(0,len(NdotD)):
            if(NdotD[i]!=0):
                theT=calculateT(i)
                t.append(theT)
                if(NdotD[i]<0):
                    NdotPoints.append("PL")
                    finaltE=t[i]
                    tEntering.append(finaltE)
                elif(NdotD[i]>0):
                    NdotPoints.append("PE")
                    finaltL=t[i]
                    tLeaving.append(finaltL)

        
        print(f"This is N points based on Ni.D sequencing left, top, right, bottom:{N}")
        print(f"This is Ni.D sequencing left, top, right, bottom: {NdotD}")
        print(f"This is PL/PE points based on Ni.D sequencing left, top, right, bottom: {NdotPoints}")
        print(f"This is all the t values sequencing left, top, right, bottom: {t}")
        print(f"These are all the tE that enters the clip window as per to PE: {tEntering}")
        print(f"These are all the tL that enters the clip window as per to PL: {tLeaving}")
        
        
        print(f"t_e max: {max(tEntering)}")
        print(f"t_l min: {min(tLeaving)}")
        print(f"Value of D: {d}")
        print("---------------------------------------------------------------")
        if(max(tEntering)>min(tLeaving)):
            print("tE is greater then tL")    
        else:
           P0_new = P(x_0,y_0,max(tEntering),d)
           P1_new = P(x_0,y_0,min(tLeaving),d)
    

    return [P0_new, P1_new], max(tEntering), min(tLeaving)


#boundary
x_min=21
y_min=42

x_max=-2
y_max=1

#points
x_0=-1
y_0=55

x_1=68
y_1=-37

result=[]
result, tE, tL=cyrusBeck(x_0,y_0,x_1,y_1)
T=tL-tE
print(f"Value of tL-tE: {T}")
x=result[0]
y=result[1]
x_2=np.square(np.subtract(x[0],y[0]))
y_2=np.square(np.subtract(x[1],y[1]))
final=x_2+y_2
print(f"Length of lineSegment: {m.sqrt(final)}")

print(f"P({tE})= {result[0]}")
print(f"P({tL})= {result[1]}")

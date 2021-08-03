# Cyrus-Beck
Clipping Algorithm using parametric equation of a line.

#Calculate D which is the differences of parametrics P(1) and P(0):
def D(x_0,y_0,x_1,y_1):
    x_D=(x_1-x_0)
    y_D=(y_1-y_0)
    D=[x_D,y_D]
    return D

#Specifies the directional matrices of left, top, right, bottom sequentially 
  #Then takes the directional matrices and dot products with the D value compiled just above
    #Stores the final matrices in a list ND
def NiD(func):
    N=[(-1,0),(0,1),(1,0),(0,-1)] #[left, top, right, bottom]
    ND=[] #[left, top, right, bottom]
    for i in range(0,len(N)):
        ND.append(np.dot(N[i],func))    
    return ND


#Calculates t values which specifies the point that intersects on the line segments
 based on the clipping window being close or far off
def calculateT(i):
    if(i==0):
        return round((-(x_0-x_min)/(x_1-x_0)),8) # t_left(x_0,x_1,x_min)
    elif(i==1):
        return round((-(x_0-x_max)/(x_1-x_0)),8) #t_right(x_0,x_1,x_max):
    elif(i==2):
        return round((-(y_0-y_max)/(y_1-y_0)),8) #t_top(y_0,y_1,y_max):
    elif(i==3):
        return round((-(y_0-y_min)/(y_1-y_0)),8) #t_bottom(y_0,y_1,y_min):


#This is the function that calculates the parametric function of each line segment after computing
  the t value and attaining the initial value, along with the D value
def P(x_0, y_0, t, func):
    D=func
    tdotD=np.dot(t,D)
    p=np.sum([[x_0,y_0],tdotD],axis=0)
    return p


#This is the cyrus-beck algo that accumulates all the other functions
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


#boundary to specify
x_min, y_min | x_max, y_max 

#points to specify
x_0, y_0 | x_1, y_1

cyrusBeck(x_0,y_0,x_1,y_1)


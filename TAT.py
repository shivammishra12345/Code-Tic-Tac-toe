# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:34:31 2020

@author: aq1
"""

        



L=[[0,1,2],[3,4,5],[6,7,8]]
print(L,"\n \n")


print(L[0][0],"|",L[0][1],"|",L[0][2])
print("__","","__","","__")
print(L[1][0],"|",L[1][1],"|",L[1][2])
print("__","","__","","__")
print(L[2][0],"|",L[2][1],"|",L[2][2])
print("Symbol are:","#,$,*,&")
c=input("First player enter your name: ")

while True:
    m=input("First player enter your symbol: ")
    if (m in ["#","$","*","&"]):
        break
    else:
        print("Enter the symbol from the given symbol")
        
        
    
b=input("Second player enter your name: ")

while True:
    n=input("Second player enter your symbol: ")
    if ((n in ["#","$","*","&"] )and (m!=n)):
        break
    else:
        print("Enter the symbol from the given symbol other than first player symbol")
        

i=0

while (0<=i<=8):
    if (i==0 or i==1 or i==2 or i==4 or i==3 or i==7or i==8):
        
        if i in [0,2,4,6,8]:
            symbol=m
        else:
            symbol=n
            
        if i==0:
            j=int(input("Enter the position"))
        else:
            j=int(input("Next player enter the position which is unmarked"))
        if j==0:
            if L[0][0]==0:
                L[0][0]=symbol
                i=i+1
                
                
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==1:
            if L[0][1]==1:
                L[0][1]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
                
        elif j==2:
            if L[0][2]==2:
                L[0][2]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                i=i-1
                
        elif j==3:
            if L[1][0]==3:
                L[1][0]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==4:
            if L[1][1]==4:
                L[1][1]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==5:
            if L[1][2]==5:
                L[1][2]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
                
        elif j==6:
            if L[2][0]==6:
                L[2][0]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
                
        elif j==7:
            
            if L[2][1]==7:
                L[2][1]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==8:
            if L[2][2]==8:
                L[2][2]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
        else:
            print("This is not an valid position")
        print(L[0][0],"|",L[0][1],"|",L[0][2])
        print("__","","__","","__")
        print(L[1][0],"|",L[1][1],"|",L[1][2])
        print("__","","__","","__")
        print(L[2][0],"|",L[2][1],"|",L[2][2])
    elif (i==5 or i==6):
        
        #h(L)
        if (L[0][0]==m and L[0][1]==m and L[0][2]==m):
            print("Congratulations you are the winner,",c)
            break
        elif (L[1][0]==m and L[1][1]==m and L[1][2]==m):
            print("Congratulations you are the winner,",c)
            break
        elif (L[2][0]==m and L[2][1]==m and L[2][2]==m):
            print("Congratulations you are the winner,",c)
            break
        elif (L[0][0]==m and L[1][0]==m and L[2][0]==m):
            print("Congratulations you are the winner,",c)
            break
        elif (L[0][1]==m and L[1][1]==m and L[2][1]==m):
            print("Congratulations you are the winner,",c)
            break
        elif (L[0][2]==m and L[1][2]==m and L[2][2]==m):
            print("Congratulations you are the winner,",c)
            break
        elif (L[0][0]==m and L[1][1]==m and L[2][2]==m):
            print("Congratulations you are the winner,",c)
            break
        elif (L[0][2]==m and L[1][1]==m and L[2][0]==m):
            print("Congratulations you are the winner,",c)
            break    
        elif (L[0][0]==n and L[0][1]==n and L[0][2]==n):
            print("Congratulations you are the winner,",b)
            break 
        elif (L[1][0]==n and L[1][1]==n and L[1][2]==n):
            print("Congratulations you are the winner,",b)
            break
        elif (L[2][0]==n and L[2][1]==n and L[2][2]==n):
            print("Congratulations you are the winner,",b)
            break
        elif (L[0][0]==n and L[1][0]==n and L[2][0]==n):
            print("Congratulations you are the winner,",b)
            break
        elif (L[0][1]==n and L[1][1]==n and L[2][1]==n):
            print("Congratulations you are the winner,",b)
            break
        elif (L[0][2]==n and L[1][2]==n and L[2][2]==n):
            print("Congratulations you are the winner,",b)
            break
        elif (L[0][0]==n and L[1][1]==n and L[2][2]==n):
            print("Congratulations you are the winner,",b)
            break
        elif (L[0][2]==n and L[1][1]==n and L[2][0]==n):
            print("Congratulations you are the winner,",b)
            break
        else:
            pass
        if i in [0,2,4,6,8]:
            symbol=m
        else:
            symbol=n
            
        j=int(input("Enter the position")) 
        if j==0:
            if L[0][0]==0:
                L[0][0]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==1:
            if L[0][1]==1:
                L[0][1]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
                
        elif j==2:
            if L[0][2]==2:
                L[0][2]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==3:
            if L[1][0]==3:
                L[1][0]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==4:
            if L[1][1]==4:
                L[1][1]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==5:
            if L[1][2]==5:
                L[1][2]=symbol
                i=i+1
            else:
                print("This position is already marked")
                i=i-1
                
                
        elif j==6:
            if L[2][0]==6:
                L[2][0]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
                
        elif j==7:
            
            if L[2][1]==7:
                L[2][1]=symbol
                i=i+1
            else:
                print("This position is already marked")
                i=i-1
                
        elif j==8:
            if L[2][2]==8:
                L[2][2]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        else:
            print("This is not an valid position")
        print(L[0][0],"|",L[0][1],"|",L[0][2])
        print("__","","__","","__")
        print(L[1][0],"|",L[1][1],"|",L[1][2])
        print("__","","__","","__")
        print(L[2][0],"|",L[2][1],"|",L[2][2]) 
    elif i==8:
        if i in [0,2,4,6,8]:
            symbol=m
        else:
            symbol=n
            
        j=int(input("Enter the position")) 
        if j==0:
            if L[0][0]==0:
                L[0][0]=symbol
                i=i+1
                
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==1:
            if L[0][1]==1:
                L[0][1]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
                
        elif j==2:
            if L[0][2]==2:
                L[0][2]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==3:
            if L[1][0]==3:
                L[1][0]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==4:
            if L[1][1]==4:
                L[1][1]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        elif j==5:
            if L[1][2]==5:
                L[1][2]=symbol
                i=i+1
            else:
                print("This position is already marked")
                i=i-1
                
                
        elif j==6:
            if L[2][0]==6:
                L[2][0]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
                
        elif j==7:
            
            if L[2][1]==7:
                L[2][1]=symbol
                i=i+1
            else:
                print("This position is already marked")
                i=i-1
                
        elif j==8:
            if L[2][2]==8:
                L[2][2]=symbol
                i=i+1
            else:
                print("This position is already marked")
                
                i=i-1
        else:
            print("This is not an valid position")
        print(L[0][0],"|",L[0][1],"|",L[0][2])
        print("__","","__","","__")
        print(L[1][0],"|",L[1][1],"|",L[1][2])
        print("__","","__","","__")
        print(L[2][0],"|",L[2][1],"|",L[2][2]) 
        print("The Match tie between ",c,"and",b)

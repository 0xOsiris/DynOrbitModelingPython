from __future__ import division
from sympy import *
from sympy.solvers import solve
from sympy import Symbol, Eq, Function
from sympy.utilities.lambdify import lambdify, implemented_function
import sympy as sim
from dill.source import getsource
import math

#######################
###  Leyton Taylor  ###
###Dynamical Systems###
###     Example     ###
#######################


functionList=[[lambda x: x**2+.25, lambda x:2*x],
[lambda x: x**2, lambda x: 2*x],
[lambda x: x**2-.24, lambda x:2*x],
[lambda x: x**2-.75, lambda x: 2*x],
[lambda x: .4*x-.4*x**2, lambda x:.4 -.8*x],
[lambda x: x*1-x**2, lambda x: -2*x+1],
[lambda x: 1.6*x-1.6*x**2, lambda x: 1.6-3.2*x],
[lambda x: 2*x-2*x**2,lambda x: 2-4*x],
[lambda x:2.4*x-2.4*x**2,lambda x: 2.4-4.8*x],
[lambda x: 3*x-3*x**2, lambda x: 3-6*x]]



def CalcOrbits(F,Df,o=.2, Epsilon=10**-2):
    fixedPoints=[0]
    temp=o
    iterationCount=0
    loop=True
    while(loop):
        lastOut=F(temp)
        temp=lastOut
        iterationCount+=1
        for p in fixedPoints:
            if(abs(temp-p)<=Epsilon):
                outT=temp
                fixedPoint=p
                loop=False 
        
      
    if(Df(fixedPoint) !=1):
        prop='Attracting'
    else:
        prop='Neutral'

    dF= Df(fixedPoint)
    return('FixedPoints: '+ str(fixedPoints)+'\n'
          + '|Df(p)|: '+str(dF)+'\n'
          + prop + '\n'
          +"Iteration Count: " +str(iterationCount)+'\n'+
           str(outT))

def calcFixedPoint(F):
    x=Symbol('x')

    return solve(F(x)-x)

def main():
    for i in range(len(functionList)):
        print('Function ' +str(getsource(functionList[i][0])))
        print(CalcOrbits(functionList[i][0], functionList[i][1])+'\n'+'-----'+'\n')
main()

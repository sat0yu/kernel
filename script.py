#coding=utf-8

import numpy
from kernel import *
from graph import *

if __name__=='__main__':

    V = numpy.loadtxt('V.txt', dtype=numpy.float)
    E = numpy.loadtxt('E.txt', dtype=numpy.int, comments='#')
    g = Graph(V, E)

    beta = 0.005
    def graphkernel(x, y):
        s = numpy.exp( -beta * (numpy.linalg.norm(x[0] - y[0])** 2))
        e = numpy.exp( -beta * (numpy.linalg.norm(x[1] - y[1])** 2))
        return s*e

    def graphkernel_2(x, y):
        s = numpy.dot( x[0], y[0] )
        e = numpy.dot( x[1], y[1] )
        return s*e


    gm = GramMatrix(g.E['data'], kernel=graphkernel)
    func = gm.regression(g.E['label'], 0.01)

    for i in range(10, 90+1, 2):
        for j in range(10, 90+1, 2):
            for u in range(10, 90+1, 2):
                for v in range(10, 90+1, 2):
                    #e = ( numpy.array((i,j)), numpy.array((u,v)) )
                    val = func(( numpy.array((i,j)), numpy.array((u,v)) ))
                    if(val > 0.5):
                        print (i,j,u,v), val

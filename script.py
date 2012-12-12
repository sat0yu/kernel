#coding=utf-8

import numpy
from kernel import *
from graph import *

if __name__=='__main__':

    V = numpy.loadtxt('V.txt', dtype=numpy.float)
    E = numpy.loadtxt('E.txt', dtype=numpy.int, comments='#')
    g = Graph(V, E)

    beta = 0.5
    def graphkernel(x, y):
        s = numpy.exp( -beta * (numpy.linalg.norm(x[0] - y[0])** 2))
        e = numpy.exp( -beta * (numpy.linalg.norm(x[1] - y[1])** 2))
        return s*e

    gm = GramMatrix(g.E['data'], kernel=graphkernel)
    func = gm.regression(g.E['label'], 0.05)

    print func( g.edge( (0,1) ) )
    print func( g.edge( (0,2) ) )
    print func( g.edge( (0,3) ) )
    print func( g.edge( (1,2) ) )
    print func( g.edge( (2,3) ) )


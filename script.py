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

    gm_2 = GramMatrix(g.E['data'], kernel=graphkernel_2)
    func_2 = gm_2.regression(g.E['label'], 0.01)

    print '\nregression edge(4, [0~8])'
    print func( g.edge( (4,0) ) ), func_2( g.edge( (4,0) ) )
    print func( g.edge( (4,1) ) ), func_2( g.edge( (4,1) ) )
    print func( g.edge( (4,2) ) ), func_2( g.edge( (4,2) ) )
    print func( g.edge( (4,3) ) ), func_2( g.edge( (4,3) ) )
    print func( g.edge( (4,4) ) ), func_2( g.edge( (4,4) ) )
    print func( g.edge( (4,5) ) ), func_2( g.edge( (4,5) ) )
    print func( g.edge( (4,6) ) ), func_2( g.edge( (4,6) ) )
    print func( g.edge( (4,7) ) ), func_2( g.edge( (4,7) ) )
    print func( g.edge( (4,8) ) ), func_2( g.edge( (4,8) ) )

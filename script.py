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

    def graphkernel_2(x, y):
        s = numpy.dot( x[0], y[0] )
        e = numpy.dot( x[1], y[1] )
        return s*e


    gm = GramMatrix(g.E['data'], kernel=graphkernel)
    func = gm.regression(g.E['label'], 0.01)

    gm_2 = GramMatrix(g.E['data'], kernel=graphkernel_2)
    func_2 = gm_2.regression(g.E['label'], 0.01)

    print '\nregression edge(8, [78~82])'
    print func( g.edge( (8,78) ) ), func_2( g.edge( (8,78) ) )
    print func( g.edge( (8,79) ) ), func_2( g.edge( (8,79) ) )
    print func( g.edge( (8,80) ) ), func_2( g.edge( (8,80) ) )
    print func( g.edge( (8,81) ) ), func_2( g.edge( (8,81) ) )
    print func( g.edge( (8,82) ) ), func_2( g.edge( (8,82) ) )

    print '\nregression edge(9, [78~82])'
    print func( g.edge( (9,78) ) ), func_2( g.edge( (9,78) ) )
    print func( g.edge( (9,79) ) ), func_2( g.edge( (9,79) ) )
    print func( g.edge( (9,80) ) ), func_2( g.edge( (9,80) ) )
    print func( g.edge( (9,81) ) ), func_2( g.edge( (9,81) ) )
    print func( g.edge( (9,82) ) ), func_2( g.edge( (9,82) ) )

    print '\nregression edge(8, [97~101])'
    print func( g.edge( (8,97) ) ), func_2( g.edge( (8,97) ) )
    print func( g.edge( (8,98) ) ), func_2( g.edge( (8,98) ) )
    print func( g.edge( (8,99) ) ), func_2( g.edge( (8,99) ) )
    print func( g.edge( (8,100) ) ), func_2( g.edge( (8,100) ) )
    print func( g.edge( (8,101) ) ), func_2( g.edge( (8,101) ) )

    print '\nregression edge(9, [97~101])'
    print func( g.edge( (9,97) ) ), func_2( g.edge( (9,97) ) )
    print func( g.edge( (9,98) ) ), func_2( g.edge( (9,98) ) )
    print func( g.edge( (9,99) ) ), func_2( g.edge( (9,99) ) )
    print func( g.edge( (9,100) ) ), func_2( g.edge( (9,100) ) )
    print func( g.edge( (9,101) ) ), func_2( g.edge( (9,101) ) )

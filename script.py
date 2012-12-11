#coding=utf-8

import numpy
from kernel import *
from graph import *

if __name__=='__main__':

#     V = numpy.array([
#             [ 1, -1, 1, -1,  1],
#             [ 1, -1, 1,  0,  1],
#             [ 1, -1, 1,  1,  0],
#             [ 1,  1, 1, -1, -1]
#             ])

    #numpy.savetxt('V.txt', V)
    V = numpy.loadtxt('V.txt', dtype=numpy.float)

    # element must be following style, (label, (sn, en))
    E = [
        ( 1, (0,1)),
        ( 1, (0,2)),
        ( 1, (0,3)),
        ( 1, (1,2)),
        (-1, (2,3)),
        ]
    numpy.savetxt('E.txt', E)
    
    g = Graph(V, E)
    def gauss(x1, x2):
        return numpy.exp( -1.0 * 0.5 * (numpy.linalg.norm(x1 - x2)** 2) )

    gm = g.grammatrix(gauss)
    func = gm.regression(g.E['label'], 0.1)

    kv = g.kernelfuncvector( g.edge( (0,1) ), gauss)
    print func( kv )
    kv = g.kernelfuncvector( g.edge( (0,2) ), gauss)
    print func( kv )
    kv = g.kernelfuncvector( g.edge( (0,3) ), gauss)
    print func( kv )
    kv = g.kernelfuncvector( g.edge( (1,2) ), gauss)
    print func( kv )
    kv = g.kernelfuncvector( g.edge( (2,3) ), gauss)
    print func( kv )


#coding=utf-8

import numpy
from kernel import *
from graph import *

if __name__=='__main__':
    V = numpy.array([[1,-1,1,-1,1],[1,-1,1,0,1],[1,-1,1,1,0],[1,1,1,-1,-1]])

    # element must be following style, (label, (sn, en))
    E = [(1,(0,1)),(1,(0,2)),(1,(0,3)),(1,(1,2)), (-1, (2,3))]
    
    g = Graph(V, E)
    y = g.E['label']

    gm = g.grammatrix()
    gkv = g.kernelfuncvector()

    print 'gram: \n', gm
    print 'label: ', y

    func = gm.regression(numpy.matrix(y).T, 1.0)

    kv = gkv( g.edge( (1,3) ) )
    print kv
    print func( numpy.matrix(kv).T )


#coding=utf-8

import numpy
import kernel

class Graph():
    def __init__(self, V, E, direct=False):
        self.V = V
        print 'the size of given V(v)ertices set:', len(V)            

        E = E if direct else Graph.duplicate(E)
        print 'the size of given E(e)dges set:', len(E)
        self.E = {}
        self.E['label'] = [ elm[0] for elm in E]
        self.E['data'] = [ self.edge(elm[1]) for elm in E]

    def edge(self, e):
        u'''
        インデックスで始点、終点を指定されたエッジをノードの実体に置き換える
        '''
        sn = en = None

        if 0 <= e[0] < len(self.V):
            sn = self.V[ e[0] ]
        else:
            print 'warning: start node does not exist in given V, given edge: ', e

        if 0 <= e[1] < len(self.V):
            en = self.V[ e[1] ]
        else:
            print 'warning: end node does not exist in given V, given edge: ', e

        return (sn, en)

    def grammatrix(self):
        nE = len(self.E['data'])
        gm = numpy.empty( (nE, nE) )
        for i, ei in enumerate(self.E['data']):
            for j, ej in enumerate(self.E['data']):
                ip_sn = numpy.dot(ei[0], ej[0])
                ip_en = numpy.dot(ei[1], ej[1])
                gm[i,j] = ip_sn * ip_en

        return kernel.GramMatrix(gm)

    def kernelfuncvector(self, e):
        kv = []
        for ei in self.E['data']:
            ip_sn = numpy.dot(ei[0], e[0])
            ip_en = numpy.dot(ei[1], e[1])
            kv.append( ip_sn * ip_en )
        return kv

    @classmethod
    def duplicate(cls, _E):
        u'''
        無向グラフのとき、もう一方向のエッジも複製する
        '''
        for e in _E:
            e = ( e[0], (e[1][1], e[1][0]) )
            if not e in _E:
                _E.append(e)
        return _E

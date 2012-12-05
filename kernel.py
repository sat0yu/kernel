#coding=utf-8

import numpy

class SquareMatrix(numpy.matrix):
    def __new__(cls, *args, **kwargs):
        ins = super(SquareMatrix, cls).__new__(cls, *args, **kwargs)

        # numpy.matrix.__new__にmatrixクラスのインスタンスを渡すと
        # 戻り値がclsのインスタンスではなくなるので__init__が呼ばれなくなる
        # これを回避するために、insのクラスを変更しておく
        if not isinstance(ins, cls):
            print 'cast to %s from %s' % (cls.__name__, ins.__class__.__name__)
            ins.__class__ = cls
 
        if cmp(*ins.shape) != 0:
            raise Exception('SquareMatrix must be square')
        else:
            ins.dim = ins.shape[0]
            return ins

    def identity(self):
        return numpy.identity(self.dim)

    def eig(self):
        return numpy.linalg.eig(self)

    def eigshift(self, s):
        print 'shift parameter s: %s' % s
        l, V = self.eig()
        D = numpy.diag(l + s)
        return  SquareMatrix(V * D * V.I)

    def fixnegative(self, upperbound):
        print 'fix negative parameter: %s' % upperbound
        l, V = self.eig()
        scale = min(l)
        if scale >= 0.0:
            print 'factors in lambda vector are all positive'
        else:
            l = [upperbound * (1 - lam/scale) if lam < 0.0 else lam for lam in l]
        
        D = numpy.diag(l)
        return  SquareMatrix(V * D * V.I)

    def exponential(self, t=1.0):
        print 'exponential parameter t: %s' % t
        l, V = self.eig()
        D = numpy.diag(numpy.exp(t * l))
        return  SquareMatrix(V * D * V.I)

class GramMatrix(SquareMatrix):
    def __init__(self, *args, **kwargs):
        # 逆行列を生成する際にも呼ばれる
        #print "GramMatrix init \nlen(args): %s, kwargs: %s" % (len(args), kwargs)
        neg = [ val for val in self.eig()[0] if val < 0 ]
        if len(neg) != 0:
            print 'Warning: this gram matrix is not a semipositive definite matrix'
            print 'Negative eigenvalues: ', neg

    def regression(self, vLabel, regParam):
        print 'regression parameter l: %s' % regParam
        vAlpha = ( self + regParam * self.identity() ).I * vLabel
        def func(vX):
            return vAlpha.T * vX

        return func

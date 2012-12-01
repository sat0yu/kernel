#coding=utf-8

import csv
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
        pass

    def regression(self, vLabel, regParam):
        print 'regression parameter l: %s' % regParam
        vAlpha = ( self + regParam * self.identity() ).I * vLabel
        def func(vX):
            return vAlpha.T * vX

        return func

def loadCSV(filename, dtype='int64'):
    dataset = {'order':[], 'variables':{}}
    
    with open(filename, 'rU') as f:
        reader = csv.reader(f)
                
        varDeclareRow = reader.next()
        varDefineRow = reader.next()
                
        # 1,2行目から、各変数の定義を読み取る
        for i, v in enumerate(varDeclareRow):
            if v:
                var = v
                dataset['order'].append(var)

            dataset['variables'].setdefault(var, {'factors':[]})
            dataset['variables'][var]['factors'].append(varDefineRow[i])

        for var in dataset['variables']:
            dataset['variables'][var]['dim'] = len(dataset['variables'][var]['factors'])

        DATA = numpy.matrix([row for row in reader], dtype=dtype)

        ps = 0
        for var in dataset['order']:
            dataset['variables'][var]['DATA'] = DATA[:,ps:ps+dataset['variables'][var]['dim']]
            ps = dataset['variables'][var]['dim']

#         for key, val in  dataset['variables'].items():
#             print key, val

    return dataset

def loadTXT(filename, delimiter=None, format=None):
    DATA =  numpy.loadtxt(filename, delimiter=delimiter)
    print DATA

    # format must be following style "{'y':(0,2), 'x':(2,12)}"
    for key,val in format.items():
        print key, DATA[:,val[0]:val[1]]

    return DATA

if __name__=='__main__':
    dataset = loadCSV('graphdata.csv')

    X = dataset['variables']['X']['DATA']
    sm = SquareMatrix(X, dtype='float64')
    print 'SquareMatrix :\n', sm
    print 'dimention: %s, shape: %s' % (sm.dim, sm.shape)
    print 'lambda: %s' % sm.eig()[0]

    ek = sm.exponential(0.1)
    print 'lambda: %s' % ek.eig()[0]
    gm = GramMatrix(ek)

#     m = min(sm.eig()[0])
#     m = -m if m < 0 else m
#     esk = sm.eigshift(m)
#     print 'lambda: %s' % esk.eig()[0]
#     gm = GramMatrix(esk)

#     upperbound = min([lam if lam > 0.0 else 0.0 for lam in sm.eig()[0]])
#     fnk = sm.fixnegative(upperbound)
#     print 'lambda: %s' % fnk.eig()[0]
#     gm = GramMatrix(fnk)

    print 'GramMatrix :\n', gm    
    label = dataset['variables']['y']['DATA'][:,0]
    func = gm.regression(label, 0.1)

    print 'Labeled Data :', label.T

    print 'Positivex :'
    x1 = numpy.matrix([0,0,0,0,0,0,0,0,0,1]).T
    print x1.T, func(x1)

    x2 = numpy.matrix([0,0,0,0,0,0,0,0,1,1]).T
    print x2.T, func(x2)

    x3 = numpy.matrix([0,0,0,0,0,0,1,0,1,1]).T
    print x3.T, func(x3)

    x4 = numpy.matrix([0,0,0,1,0,0,1,0,1,1]).T
    print x4.T, func(x4)

    x5 = numpy.matrix([0,0,1,1,0,0,1,0,1,1]).T
    print x5.T, func(x5)

    x6 = numpy.matrix([1,0,1,1,0,0,1,0,1,1]).T
    print x6.T, func(x6)

    print 'Negative :'
    x1 = numpy.matrix([0,0,0,0,0,0,0,1,0,0]).T
    print x1.T, func(x1)

    x2 = numpy.matrix([0,0,0,0,0,1,0,1,0,0]).T
    print x2.T, func(x2)

    x3 = numpy.matrix([0,0,0,0,1,1,0,1,0,0]).T
    print x3.T, func(x3)

    x4 = numpy.matrix([0,1,0,0,1,1,0,1,0,0]).T
    print x4.T, func(x4)

#     print 'Mixed :'
#     for i in xrange(2**10):
#         li = [int(c) for c in format(i, '010b')]
#         x = numpy.matrix(li).T
#         print x.T, func(x)

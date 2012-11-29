#coding=utf-8

import csv
import numpy
import math

class DiffusionKernel():
    def __init__(self, t, L):
        self.__t = t
        self.__L = numpy.matrix(L, dtype=numpy.float)

        n,m = self.__L.shape
        if n != m:
            print 'L must be square matrix.'
            return None
        else:
            self.__dim = n

        print 'L :'
        print self.__L

        l,v = numpy.linalg.eig(self.__L)
        print 'lambda :'
        print l

        self.__tL = self.__t * self.__L
#         print 'tL :'
#         print self.__tL
         
    def exp_term(self, n):
        return self.__tL**n / math.factorial(n)
            
    def difussion1(self, n = 20):
        L = numpy.identity(self.__dim)
        for i in xrange(1,n):
            try:
                L += self.exp_term(i)
            except TypeError:
                print 'tL**%s ~ 0' % i
                break
        return L

    def difussion2(self):
        l, V = numpy.linalg.eig(self.__L)
        D = numpy.diag(numpy.exp(self.__t * l))
        return  V * D * V.I

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
#     a = DiffusionKernel(0.1, [[-2, 1, 1, 0],[1, -2, 1, 0],[1, 1, -3, 1],[0, 0, 1, -1]])
#     print "exp(tL) = V * exp(tD) * V-1 :"
#     print a.difussion2()
#     print 'exp(tL; 50) :'
#     print a.difussion1(50)

    dataset = loadCSV('graphdata.csv')
    DK = DiffusionKernel(0.1, dataset['variables']['X']['DATA'])
    print DK.difussion2()

#     loadTXT('graphdata.txt', delimiter=',', format={'y':(0,2), 'x':(2,12)})

#coding=utf-8

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
        print 'tL :'
        print self.__tL
         
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

if __name__=='__main__':
    a = DiffusionKernel(0.25, [[-2,1,1,0,0],[1,-2,0,1,0],[1,0,-2,1,0],[0,1,1,-3,1],[0,0,0,1,-1]])
#    a = DiffusionKernel(0.1, [[-2, 1, 1, 0],[1, -2, 1, 0],[1, 1, -3, 1],[0, 0, 1, -1]])

#     print 'exp(tL; 50) :'
#     print a.difussion1(50)

    print "exp(tL) = V * exp(tD) * V-1 :"
    print a.difussion2()

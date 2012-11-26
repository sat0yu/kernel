#coding=utf-8

import numpy
import math

class DiffusionKernel():
    def __init__(self, t, L):
        self.__n = 0
        self.__t = t
        self.__rawL = numpy.matrix(L, dtype=numpy.float)

        print 'L :'
        print self.__rawL        

        n,m = self.__rawL.shape
        if n != m:
            print 'L must be square matrix.'
            return None
        else:
            self.__dim = n

        self.__L = numpy.identity(self.__dim)
        self.__tL = self.__t * self.__rawL

#         print 'n :', self.__n
        print 'tL :'
        print self.__tL
#         print 'L :', self.__L
         
    def next(self):
        self.__n += 1
        try:
            self.__L += self.__tL**self.__n / math.factorial(self.__n)
        except TypeError:
            print '!!! tL**n ~ 0'

        print 'n :', self.__n
        print 'L :', self.__L
            
    def factorialize(self):
        l, V = numpy.linalg.eig(self.__rawL)
        D = numpy.diag(l)
        return D, V

    def difussion(self):
        l, V = numpy.linalg.eig(self.__rawL)
        D = numpy.diag(l)        
        return V * numpy.exp(self.__t * D) * V.I

if __name__=='__main__':
    a = DiffusionKernel(0.25, [[1,2,3,4],[2,3,4,5],[-1,-2,-3,-4],[-2,-3,-4,-5]])
#     a = DiffusionKernel(0.25, [[-2, 1, 1, 0],[1, -2, 1, 0],[1, 1, -3, 1],[0, 0, 1, -1]])

    for i in xrange(20):
        a.next()

#     D, V = a.factorialize()
#     print 'tL = t(V*D*V-1)'
#     print "D :"
#     print D
#     print 'V :'
#     print V
#     print 'V * D * V-1'
#     print V*D*V.I

    print "exp(tL) = V * exp(tD) * V-1:"
    print a.difussion()

#coding: utf-8

import sys
import numpy
from pylab import *

class GaussKernel():
    def __init__(self, beta):
        self.__beta = beta

    def val(self, vec1, vec2):
        dist = numpy.linalg.norm(vec1-vec2)
        return numpy.exp(-self.__beta*(dist**2))

    def gram(self, X):
        N = len(X)
        gm = numpy.identity(N)
        for i in xrange(N):
            for j in xrange(N):
                if(i != j and not gm[i][j]):
                    gm[j][i] = gm[i][j] = self.val(X[i], X[j])
        return gm

if __name__ == '__main__':
    argv = sys.argv
    if(len(argv) == 1):
        print 'need an argument that means a wave filename'
        quit()
    filename = argv[1] 

    try:
        X = numpy.loadtxt(filename)
        N = len(X)
    except IOError:
        print '%s: cannot open' % filename
    
    gk01 = GaussKernel(0.1)
    gk0001 = GaussKernel(0.001)
    # グラム行列
    GM01 = gk01.gram(X)
    GM0001 = gk0001.gram(X)

    J = numpy.identity(N) - (1.0/N)* numpy.ones((N,N))
    JK01 = numpy.dot(J, GM01)
    JK0001 = numpy.dot(J, GM0001)

    # 固有値固有ベクトル
    la01, V01 = numpy.linalg.eig(JK01)
    la0001, V0001 = numpy.linalg.eig(JK0001)
    #subplot(121)
    #plot(la01)
    #subplot(122)
    #plot(la0001)
    #show()

    # 各入力を写像した値
    f01_1 = numpy.zeros(N)
    f01_2 = numpy.zeros(N)
    f0001_1 = numpy.zeros(N)
    f0001_2 = numpy.zeros(N)
    
    alpha01_1 = V01[:, N-1]
    alpha01_2 = V01[:, N-2]
    alpha0001_1 = V0001[:, N-1]
    alpha0001_2 = V0001[:, N-2]
    for i in xrange(N):
        for j in xrange(N):
            f01_1[i] += alpha01_1[j] * gk01.val(X[j], X[i])
            f01_2[i] += alpha01_2[j] * gk01.val(X[j], X[i])
            f0001_1[i] += alpha0001_1[j] * gk0001.val(X[j], X[i])
            f0001_2[i] += alpha0001_2[j] * gk0001.val(X[j], X[i])

    subplot(121)
    plot(f01_1, f01_2, marker="o")
    subplot(122)
    plot(f0001_1, f0001_2, marker="o")
    show()

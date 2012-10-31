#coding: utf-8

import sys
import numpy
from pylab import *
import random
from mpl_toolkits.mplot3d import Axes3D

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

def swiss_role(N):
    label = numpy.ones(N)
    swiss = numpy.zeros((N, 3))
    for i in xrange(N):
        r1 = random.uniform(-1.0, 1.0)
        r2 = random.uniform(-1.0, 1.0)
        swiss[i, 0] = numpy.sqrt(2.0 + 2.0 * r1) * numpy.cos(2.0 * numpy.pi * numpy.sqrt(2.0 + 2.0 * r1))
        swiss[i, 1] = numpy.sqrt(2.0 + 2.0 * r1) * numpy.sin(2.0 * numpy.pi * numpy.sqrt(2.0 + 2.0 * r1))
        swiss[i, 2] = 2.0 * r2
        if swiss[i, 0] > -1.2 and swiss[i, 1] < 0.0: label[i] = 2
        if swiss[i, 0] > -0.8 and swiss[i, 0] < 1.2 and swiss[i, 1] > -1.0 and swiss[i, 1] < 1.0: label[i] = 0

    return label, swiss

if __name__ == '__main__':
    # スイスロール生成
    label, X = swiss_role(500)
    # スイスロール表示
#     fig = figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.scatter(X[label==0, 0], X[label==0, 1], X[label==0, 2], c='red', marker='o')
#     ax.scatter(X[label==1, 0], X[label==1, 1], X[label==1, 2], c='blue', marker='o')
#     ax.scatter(X[label==2, 0], X[label==2, 1], X[label==2, 2], c='green', marker='o')
#     show()

    # カーネルインスタンス生成
    gk1 = GaussKernel(1)
    gk2 = GaussKernel(0.1)
    gk3 = GaussKernel(0.001)

    # グラム行列
    N = len(X)
    K1 = gk1.gram(X)
    K2 = gk2.gram(X)
    K3 = gk3.gram(X)

    J = numpy.identity(N) - (1.0/N)* numpy.ones((N,N))
    JK1 = numpy.dot(J, K1)
    JK2 = numpy.dot(J, K2)
    JK3 = numpy.dot(J, K3)

    # 固有値固有ベクトル
    la1, V1 = numpy.linalg.eig(JK1)
    la2, V2 = numpy.linalg.eig(JK2)
    la3, V3 = numpy.linalg.eig(JK3)

    # 各入力を写像した値
    swiss_2d_1 = numpy.zeros((N,2))
    swiss_2d_2 = numpy.zeros((N,2))
    swiss_2d_3 = numpy.zeros((N,2))
    
    # 写像軸ベクトル
    alpha1 = (V1[:, 0], V1[:, 1])
    alpha2 = (V2[:, 0], V2[:, 1])
    alpha3 = (V3[:, 0], V3[:, 1])

    # 写像
    for i in xrange(N):
        for j in xrange(N):
            swiss_2d_1[i, 0] += alpha1[0][j] * gk1.val(X[j], X[i])
            swiss_2d_1[i, 1] += alpha1[1][j] * gk1.val(X[j], X[i])
            swiss_2d_2[i, 0] += alpha2[0][j] * gk2.val(X[j], X[i])
            swiss_2d_2[i, 1] += alpha2[1][j] * gk2.val(X[j], X[i])
            swiss_2d_3[i, 0] += alpha3[0][j] * gk3.val(X[j], X[i])
            swiss_2d_3[i, 1] += alpha3[1][j] * gk3.val(X[j], X[i])

    # 結果表示
    subplot(221)
    scatter(swiss_2d_1[label==0, 0], swiss_2d_1[label==0, 1], c='red', marker='o')
    scatter(swiss_2d_1[label==1, 0], swiss_2d_1[label==1, 1], c='blue', marker='o')
    scatter(swiss_2d_1[label==2, 0], swiss_2d_1[label==2, 1], c='green', marker='o')
    axis([min(swiss_2d_1[:,0]), max(swiss_2d_1[:,0]), min(swiss_2d_1[:,1]), max(swiss_2d_1[:,1])])

    subplot(222)
    scatter(swiss_2d_2[label==0, 0], swiss_2d_2[label==0, 1], c='red', marker='o')
    scatter(swiss_2d_2[label==1, 0], swiss_2d_2[label==1, 1], c='blue', marker='o')
    scatter(swiss_2d_2[label==2, 0], swiss_2d_2[label==2, 1], c='green', marker='o')
    axis([min(swiss_2d_2[:,0]), max(swiss_2d_2[:,0]), min(swiss_2d_2[:,1]), max(swiss_2d_2[:,1])])

    subplot(223)
    scatter(swiss_2d_3[label==0, 0], swiss_2d_3[label==0, 1], c='red', marker='o')
    scatter(swiss_2d_3[label==1, 0], swiss_2d_3[label==1, 1], c='blue', marker='o')
    scatter(swiss_2d_3[label==2, 0], swiss_2d_3[label==2, 1], c='green', marker='o')
    axis([min(swiss_2d_3[:,0]), max(swiss_2d_3[:,0]), min(swiss_2d_3[:,1]), max(swiss_2d_3[:,1])])

    show()

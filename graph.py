#coding=utf-8

import numpy
import kernel

class Graph():
    def __init__(self, _V, _LE, direct=False):
        u'''
        _V: ノードリスト、各行がノードのデータベクトルとなる
        _LE: エッジリスト、各行は次の書式に従う'{label} {startnode} {endnode}'
        direct: 有向・無向を表すフラグ、無向の場合には自動でエッジが複製される
        '''

        self.V = _V
        print 'the size of given V(v)ertices set:', len(_V)

        # テキストから読み込んだデータを整形
        _LE = _LE if direct else Graph.duplicate(_LE)
        _L = _LE[:, 0]
        _E = _LE[:, 1:]
        E = [ (l, e) for l, e in zip(_L, _E) ]
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

    @classmethod
    def duplicate(cls, _LE):
        u'''
        無向グラフのとき、もう一方向のエッジも複製する
        '''

        # 重複判定のためにタプルリストに変換
        le_list = [(le[0], le[1], le[2]) for le in _LE]

        for le in le_list:
            # 逆方向でラベルの等しいエッジ
            rle = ( le[0], le[2], le[1] )
            if not rle in le_list:
                _LE = numpy.vstack((_LE, rle))

        return _LE

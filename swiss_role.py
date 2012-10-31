#coding: utf-8

import math
import random
import numpy
import pylab

def swiss_role(N):
  label = numpy.ones(N)
  swiss = numpy.zeros((N, 3))
  for i in xrange(N):
    r1 = random.uniform(-1.0, 1.0)
    r2 = random.uniform(-1.0, 1.0)
    swiss[i, 0] = math.sqrt(2.0 + 2.0 * r1) * math.cos(2.0 * math.pi * math.sqrt(2.0 + 2.0 * r1))
    swiss[i, 1] = math.sqrt(2.0 + 2.0 * r1) * math.sin(2.0 * math.pi * math.sqrt(2.0 + 2.0 * r1))
    swiss[i, 2] = 2.0 * r2
    if swiss[i, 0] > -1.2 and swiss[i, 1] < 0.0: label[i] = 2
    if swiss[i, 0] > -0.8 and swiss[i, 0] < 1.2 and swiss[i, 1] > -1.0 and swiss[i, 1] < 1.0: label[i] = 0

  return label, swiss

if __name__ == '__main__':
    label, data = swiss_role(2000)
    print label
    numpy.savetxt('swiss_role', data)

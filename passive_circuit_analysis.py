
import numpy as np

def Zr(r):
    return r

def Zc(c, s):
    return 1.0/(s*c)

def Zl(l, s):
    return s*l

def series(*args):
    sum = 0
    for arg in args:
        sum += arg

    return sum

def parallel(*args):
    sum = 0
    for arg in args:
        sum += 1.0/arg

    return 1.0/sum

def voltage_divider(zs, zl):
    return zl/(zs+zl)

def get_frequencies(**kwargs):
    if kwargs is None:
        return

    if 'start' in kwargs:
        print(kwargs['start'])

    if 'stop' in kwargs:
        print(kwargs['stop'])

    if 'step' in kwargs:
        print(kwargs['step'])

    if 'num_points' in kwargs:
        print(kwargs['num_points'])

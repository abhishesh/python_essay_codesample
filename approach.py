"""
Taken from : Python Patterns - An Optimization Anecdote
https://www.python.org/doc/essays/list2str/
"""


import time
import string
import array

GLOBAL_PROFILING_FLAG = True


def notimeit(method):
    "Don't profile the code"
    return method


def timeit(method):
    "Profile the code. Measure time upto 1/10th of second"
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        # print '%r (%r, %r) %2.20f sec' % (method.__name__, args, kw, te - ts)
        print '%r --- %2.20f sec' % (method.__name__, te - ts)
        return result

    return timed


# Flag to set profiling on. Accepts True or False
profile = timeit if GLOBAL_PROFILING_FLAG else notimeit


@profile
def f1(list):
    string = ""
    for item in list:
        string = string + chr(item)
    return string


@profile
def f2(list):
    return reduce(lambda string, item: string + chr(item), list, "")


@profile
def f3(list):
    string = ""
    for character in map(chr, list):
        string = string + character
    return string


@profile
def f4(list):
    string = ""
    lchr = chr
    for item in list:
        string = string + lchr(item)
    return string


@profile
def f5(list):
    string = ""
    for i in range(0, 100, 10):
        s = ""
        for character in map(chr, list[i:i + 10]):
            s = s + character
        string = string + s
    return string


@profile
def f6(list):
    return string.joinfields(map(chr, list), "")


@profile
def f7(list):
    return array.array('B', list).tostring()


# Call the functions
dummy_list = [x for x in range(100)]

f1(dummy_list)
f2(dummy_list)
f3(dummy_list)
f4(dummy_list)
f5(dummy_list)
f6(dummy_list)
f7(dummy_list)

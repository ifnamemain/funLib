import ctypes as c
import numpy as np
import time

funLib = c.cdll.LoadLibrary('./funLib.so')
funLib.getSum.restype = c.c_ulonglong
funLib.getSum.argtypes = [c.POINTER(c.c_longlong), c.c_ulong]

class fun():
  def __init__(self):
    self.arrSum = None
    return 
  def getArrSum(self, arr, arrSize, algorithm = 'c'):
    if algorithm == 'c':
      arrSum = funLib.getSum(arr.ctypes.data_as(c.POINTER(c.c_longlong)), arrSize)
    else:
      arrSum = np.sum(arr)
    self.arrSum = arrSum
    return arrSum

if __name__ == '__main__':
  arrSize = 100
  arr = np.random.randint(10, size = arrSize)
  myFun = fun()
  t = []
  t.append(time.time())
  myFun.getArrSum(arr, arr.size)
  t.append(time.time())
  print "C Sum: ", myFun.arrSum
  myFun.getArrSum(arr, arrSize, algorithm = 'np')
  t.append(time.time())
  print "np Sum: ", myFun.arrSum
  t = np.array(t)
  runTimes = np.diff(t)
  print runTimes
  

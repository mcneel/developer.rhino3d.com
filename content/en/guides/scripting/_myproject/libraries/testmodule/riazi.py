""" math library"""
import numpy

def add(x, y):
  return x + y

def numpy_random():
    return numpy.random.rand(10)[0]

if __name__ == "__main__":
    assert add(21, 21) > 0
    print(f"[ OK ] True")

import ctypes as C
mylib = C.CDLL('./libmytest.so')

mylib.add_float.restype = C.c_float
mylib.add_float.argtypes = [C.c_float, C.c_float]
mylib.add_int.restype = C.c_int
mylib.add_int.argtypes = [C.c_int, C.c_int]

# Test add_float
res = mylib.add_float(3, 4)
print  "res de add_float: ", res

# Test add_int
res = mylib.add_int(3, 4)
print  "res de add_int: ", res

# Test add_int_ref
tres = C.c_int(30)
cuatro = C.c_int(4)
res = C.c_int()
mylib.add_int_ref(C.byref(tres), C.byref(cuatro), C.byref(res))

print  "res de add_int_ref: ", res.value


# Test add_float_ref
tres = C.c_float(30)
cuatro = C.c_float(4)
res = C.c_float()
mylib.add_float_ref(C.byref(tres), C.byref(cuatro), C.byref(res))

print "res de add_float_ref: ", res.value


import numpy as np

intp = C.POINTER(C.c_int)

in1 = np.array([1, 2, -5], dtype=C.c_int)
in2 = np.array([-1, 3, 3], dtype=C.c_int)
out = np.zeros(len(in1), dtype=C.c_int)

mylib.add_int_array(in1.ctypes.data_as(intp), 
                    in2.ctypes.data_as(intp), 
                    out.ctypes.data_as(intp), 
                    C.c_int(len(out)))

print 'out de add_int_array: ',  out

flp = C.POINTER(C.c_float)
in1 = np.array([1, 2, -5], dtype=C.c_float)
in2 = np.array([-1, 3, 3], dtype=C.c_float)
out = np.zeros(len(in1), dtype=C.c_float)


mylib.dot_product.restype = C.c_float
out = mylib.dot_product(in1.ctypes.data_as(flp), 
                    in2.ctypes.data_as(flp), 
                    C.c_int(len(out)))


print  'out de dot_product: ', out

import numpy as np
import scipy
import sympy as sym
import matplotlib
import sklearn
sym.init_printing()

# print("NumPy version:", np.__version__)
# print("SciPy version:", scipy.__version__)
# print("SymPy version:", sym.__version__)
# print("Matplotlib version:", matplotlib.__version__)
# print("SkLearn version:", sklearn.__version__)

x_11,x_12,x_13 = sym.var('x_11 x_12 x_13')
x_21,x_22,x_23 = sym.var('x_21 x_22 x_23')
x_31,x_32,x_33 = sym.var('x_31 x_32 x_33')
M = sym.Matrix([[x_11,x_12,x_13],[x_21,x_22,x_23],[x_31,x_32,x_33]])
# print(np.array(M))

v_1, v_2, v_3 = sym.var('v_1, v_2, v_3')
V = sym.Matrix([[v_1],[v_2],[v_3]])
N1 = M.dot(V)
print(N1)
N2 = M.multiply(V)
print(N2)
N3 = M*V
print(N3)
# N4 =np.matmul(M,V)
# print(N4)
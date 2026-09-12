import numpy as np
a=[10,20,30,50]
b=[1,2,3,4]
n2=np.array([a,b])
print(n2)
print(type(n2))
print("dimentions")
print("size of array n2", n2.size)
print("shape of array n2",n2.shape)
n3=np.arrange(24)
print("n3",n3)
print(n3)
n3.np.arrange(1,24,2)
print(n3)
n4=np.ones(4)
print(n4)
print(n4.dtype)

n5=np.ones((3,4),dtype=int)
print(n5)
print(n5.dtype)
print(n5.ndim)

n6=np.zeros(4)
print(n6)

n6=np.zeros((3,4),dtype=int)
print(n6)
print(n6.dtype)
print(n6.ndim)

n8=np.linspace(10,20)
print(n8)

import torch

x = torch.tensor([1.0,2.0,3.0])

print(x)
print(type(x))
print("shape:",x.shape)
print("dtype:",x.dtype)
print("device:",x.device)

x = torch.tensor([
    [1.0,2.0,3.0],
    [4.0,5.0,6.0]
])

print("\n x:")
print(x)
print("x.shape:",x.shape)
print("x.ndim:",x.ndim)

X = torch.tensor([
    [1.0,2.0],
    [3.0,4.0]
])

W = torch.tensor([
    [0.5],
    [1.0]
])

Y = X @ W

print("\n矩阵乘法：")
print("X.shape:", X.shape)
print("W.shape:", W.shape)
print("Y.shape:", Y.shape)
print("Y:")
print(Y)

x = torch.tensor(2.0,requires_grad=True)

y = x ** 2

print("\nx=",x)
print("y=",y)

y.backward()

print("x.grad = ",x.grad)

w = torch.tensor(2.0,requires_grad=True)
x = torch.tensor(3.0)
b = torch.tensor(1.0,requires_grad=True)

y = w * x + b

print("\ny=",y)

y.backward()

print("w.grad =",w.grad)
print("b.grad =",b.grad)
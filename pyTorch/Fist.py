import torch

dtype = torch.float;
drive = torch.device("cpu");

a = torch.randn(2,3,device=drive,dtype=dtype)
b = torch.randn(2,3,device=drive,dtype=dtype)

print("张量a:" )
print(a)

print("张量b:")
print(b)

print("a 和 b 逐元素相乘")
print(a*b)


print("张量 a的元素总和")
print(a.sum())

print("张量a的第2行，第3列")
print(a[1,2])

print("张量a的最大值")
print(a.max())
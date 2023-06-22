import torch

#initializing tensors
device="cuda" if torch.cuda.is_available() else "cpu"

my_tensor=torch.tensor(([1,2,3],[4,5,6]),dtype=torch.float32,device=device)
print(my_tensor)


#other initialization techniques
x=torch.empty(size=(3,3))
print(x)
x=torch.zeros((3,3))
print(x)
x=torch.rand(size=(3,3))
print(x)
x=torch.ones(size=(3,3))
print(x)
x=torch.eye(5,5)
print(x)
x=torch.arange(start=0,end=5,step=1)
print(x)
x=torch.empty(size=(3,3)).normal_(mean=0,std=1)
print(x)

#how to initialize and convert tensors to different types
tensor=torch.arange(4)
print(tensor.bool())#convert to bool
print(tensor.short()) #convert to int16
print(tensor.long())#convert to int 64
print(tensor.half()) #convert to float16
print(tensor.float())
print(tensor.double()) #float64


import numpy as np
np_array=np.zeros((5,5))
tensor=torch.from_numpy(np_array)
np_array_back=tensor.numpy()
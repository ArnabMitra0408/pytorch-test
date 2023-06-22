import torch
batch_size=10
features=25
x=torch.rand((batch_size,features))
print(x.shape)
print(x[0].shape)
print(x[:,0].shape)
print(x[2,0:10])
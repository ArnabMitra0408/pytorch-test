import torch
x=torch.tensor([1,2,3])
y=torch.tensor([3,4,5])

#add
z1= torch.empty(3)
torch.add(x,y,out=z1)
print(z1)

z2=torch.add(x,y)
print(z2)

z=x+y
print(z)

#sub
z=x-y

#div
z=torch.true_divide(x,y) #element wise division

#inplace operations
t=torch.zeros(3)
t.add_(x) #inplace functions are shown by _
t+=x

#exponent
z=x.pow(2)
z= x**2

#comparison
z=x>0
print(z)
z=x<0
print(z)

#matrix multiplication
x1=torch.rand((2,5))
x2=torch.rand((5,3))
x3=torch.mm(x1,x2)

x3=x1.mm(x2)

#matrix exponentiation
matrix_exp=torch.rand(5,5)
matrix_exp.matrix_power(3)

#element wise multiplication
z=x*y

#dot product
z=torch.dot(x,y)

#batch matrix multiplication
batch=32
n=10
m=20
p=30
tensor1=torch.rand((batch,n,m))
tensor2=torch.rand((batch,m,p))
out_bmm=torch.bmm(tensor1,tensor2) #resulting shape (batch,n,p)

#broadcasting
x1=torch.rand((5,5))
x2=torch.rand((1,5))
z=x1-x2
z=x1**x2

#other operations
sum_x=torch.sum(x,dim=0)
values,indices=torch.max(x,dim=0)
values,indices=torch.min(x,dim=0)

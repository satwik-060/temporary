import torch
import numpy as np
# x = torch.rand(2,5,6,6)
# x= torch.rand(2,4,2)
# x = torch.zeros(2,2)
# x = torch.ones(2,5,dtype = torch.float32)
# x = torch.tensor([2,23.3])
# print(x)

# x = torch.rand(2,2)
# y = torch.rand(2,2)
# print(x)
# print(y)
# z = x + y 
# z = torch.add(x,y) #add , mul 
# y.add_(x)
# print(y)
# print(z)

# x = torch.rand(4,5)
# print(x)
# print(x[:,1])
# print(x[0,1])

# x = torch.rand(4,4)
# print(x)
# y = x.view(4,-1)
# print(y)

# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(b)
# a.add_(1)
# print(a)
# print(b)

# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)
# a+=1
# print(a)
# print(b)
print(torch.cuda.is_available())
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5,device = device)
    y = torch.ones(5)
    y = y.to(device)
    z = x + y
    z = z.to("cpu")
    print(z)
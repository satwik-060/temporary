import torch

# x = torch.randn(3,requires_grad = True)
# print(x)

# y = x + 2
# print(y)

# z = y * y * 2
# z  = z.mean()
# print(z)

# v = torch.tensor([0.1,1.0,0.001] , dtype = torch.float32)
# z.backward()
# print(x.grad)

# y = x.detach()
# x.requires_grad_(False)
# print(x)
# print(y)

# with torch.no_grad():
#     y = x + 2
#     print(y)

weights = torch.ones(4,requires_grad = True)

for epoch in range(1):
    model_output = (weights + 3 ).sum()
    model_output.backward()
    
    print(weights.grad)
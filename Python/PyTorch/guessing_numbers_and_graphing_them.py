from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layer = torch.nn.Linear(1, 1)

    def forward(self, x):
        x = self.layer(x)
        return x


net = Net()
print(net)

# Create and then visualize the test data
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.sin(x) * np.power(x, 3) + 3 * x + np.random.rand(100) * 0.8

plt.scatter(x, y)
plt.show()

# Convert the numpy array to tensor in shape of input size
x = torch.from_numpy(x.reshape(-1, 1)).float()
y = torch.from_numpy(y.reshape(-1, 1)).float()
print(x, y)

# Define Optimizer and Loss Function
optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
loss_func = torch.nn.MSELoss()

# Begin training
inputs = Variable(x)
outputs = Variable(y)
for i in range(250):
    prediction = net(inputs)
    loss = loss_func(prediction, outputs)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if i % 10 == 0:
        # Plot and show the learning process graphically.
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=2)
        plt.text(0.5, 0, 'Loss=%4f' % loss.data.numpy(), fontdict={'size': 10, 'color': 'red'})
        plt.pause(0.1)

plt.show()

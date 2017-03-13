import torch
import torch.nn as nn
from torch import np
from torch.autograd import Variable

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 3, 3, 100, 1

# Create random Tensors to hold inputs and outputs, and wrap them in Variables.
# TO CHANGE TO OUR INPUTS
input = [[1,2,3], [1,4,5], [6,7,8]]
x = Variable(torch.Tensor(input))
y = Variable(torch.Tensor([0,1,0]), requires_grad=False)

# Use the nn package to define our model as a sequence of layers. nn.Sequential
# is a Module which contains other Modules, and applies them in sequence to
# produce its output. Each Linear Module computes output from input using a
# linear function, and holds internal Variables for its weight and bias.
model = nn.Sequential(
          nn.Linear(D_in, H),
          nn.ReLU(),
          nn.Linear(H, D_out),
        )

# The nn package also contains definitions of popular loss functions; in this
# case we will use Mean Squared Error (MSE) as our loss function.
loss_fn = nn.MSELoss(size_average=False)

learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
for i in range(20):
    x = Variable(torch.Tensor(input))
    y = Variable(torch.Tensor([0,1,0]), requires_grad=False)
    for t in range(500):
      # Forward pass: compute predicted y by passing x to the model. Module objects
      # override the __call__ operator so you can call them like functions. When
      # doing so you pass a Variable of input data to the Module and it produces
      # a Variable of output data.
      y_pred = model(x)

      # Compute and print loss. We pass Variables containing the predicted and true
      # values of y, and the loss function returns a Variable containing the loss.
      loss = loss_fn(y_pred, y)
    #   print(t, loss.data[0])

      # Zero the gradients before running the backward pass.
      optimizer.zero_grad()

      # Backward pass: compute gradient of the loss with respect to all the learnable
      # parameters of the model. Internally, the parameters of each Module are stored
      # in Variables with requires_grad=True, so this call will compute gradients for
      # all learnable parameters in the model.
      loss.backward()

      optimizer.step()
print(x)
print(y)
input = Variable(torch.Tensor([[1,2,3], [1,4,5], [6,7,8]]))
output = model(input)
print(output)

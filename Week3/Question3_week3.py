# Deploying softmax function with class
import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        data = torch.Tensor(x)  # create a Tensor output
        # define dimension of Softmax. dim=0 means 1 -dimension
        softmax_function = nn.Softmax(dim=0)
        output = softmax_function(data)
        return output


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3000000000])
    my_softmax = MySoftmax()
    output_ex = my_softmax(data)
    assert round(output_ex[0].item(), 2) == 0.0
    print(output_ex)

# Deploying softma function
import torch
import torch.nn as nn


def softmax_func(num_list):
    data = torch.Tensor(num_list)  # create a Tensor output
    # define dimension of Softmax. dim=0 means 1 -dimension
    softmax_function = nn.Softmax(dim=0)
    output = softmax_function(data)
    return output


if __name__ == "__main__":
    list_number = [1, 2, 3]
    output_ex = softmax_func(list_number)
    assert round(output_ex[0].item(), 2) == 0.09
    print(output_ex)

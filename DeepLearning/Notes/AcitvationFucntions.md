# Activation Functions in Neural Networks

## Introduction

Activation functions are mathematical equations that determine the output of a neural network. The function is attached to each neuron in the network, and determines whether it should be activated (“fired”) or not, based on whether each neuron’s input is relevant for the model’s prediction. Activation functions also help normalize the output of each neuron to a range between 1 and 0 or between -1 and 1.

## Types of Activation Functions

### 1. Sigmoid

The sigmoid function, also called the logistic function, is traditionally a very popular activation function for neural networks. The output of the sigmoid function is in the range (0, 1). It is especially used in binary classification problems, where the output is a probability value between 0 and 1.

### 2. Tanh

The tanh function is very similar to the sigmoid function. The only difference is that it is symmetric around the origin. The range of the tanh function is (-1, 1). This makes it zero centered, and hence the gradients are centered around zero. This makes optimization easier, because the gradients have a consistent sign.

### 3. ReLU

The ReLU function is the Rectified Linear Unit activation function. It is the most widely used activation function. The ReLU function is defined as f(x) = max(0, x). The function returns 0 if it receives any negative input, but for any positive value x, it returns that value back. So it can be written as f(x) = max(0, x).

### 4. Leaky ReLU

The Leaky ReLU function is an improved version of the ReLU function. The function allows a small, positive gradient when the input is negative. The function is defined as f(x) = x if x > 0 and f(x) = ax if x <= 0. The value of a is very small, usually 0.01.

### 5. Softmax

The softmax function is often used in the final layer of a neural network-based classifier. The function takes as input a vector of K real numbers, and normalizes it into a probability distribution consisting of K probabilities proportional to the exponentials of the input numbers. The output of the softmax function is equivalent to a categorical probability distribution, it tells you the probability that any of the classes are true.

### 6. Swish

The Swish function is a new, self-gated activation function discovered by researchers at Google. The function is defined as f(x) = x \* sigmoid(x). The function is non-monotonic (meaning it is not always increasing or always decreasing) and can be used as an activation function in a neural network.

### 7. ELU

The ELU function is the Exponential Linear Unit activation function. The function is defined as f(x) = x if x > 0 and f(x) = a(e^x - 1) if x <= 0. The value of a is usually 1. The function is similar to the ReLU function, but it has a small negative output when x < 0, which helps the gradient to flow more consistently.

### 8. GELU

The GELU function is the Gaussian Error Linear Unit activation function. The function is defined as f(x) = 0.5x(1 + tanh(sqrt(2/pi)(x + 0.044715x^3))). The function is similar to the Swish function, but it has a Gaussian noise term added to it. The function is used in the GPT-2 model.

### 9. Mish

The Mish function is a new activation function discovered by researchers at Google. The function is defined as f(x) = x \* tanh(softplus(x)). The function is non-monotonic and can be used as an activation function in a neural network.

### 10. PReLU

The PReLU function is the Parametric Rectified Linear Unit activation function. The function is defined as f(x) = x if x > 0 and f(x) = ax if x <= 0. The value of a is learned during training.

### 11. RReLU

The RReLU function is the Randomized Leaky Rectified Linear Unit activation function. The function is defined as f(x) = x if x > 0 and f(x) = ax if x <= 0. The value of a is randomly sampled from a uniform distribution during training.

### 12. SELU

The SELU function is the Scaled Exponential Linear Unit activation function. The function is defined as f(x) = lambda _ x if x > 0 and f(x) = lambda _ alpha \* (e^x - 1) if x <= 0. The values of lambda and alpha are usually 1.67326 and 1.0507, respectively. The function is used in the SNN model.

### 13. CELU

The CELU function is the Continuously Differentiable Exponential Linear Unit activation function. The function is defined as f(x) = x if x > 0 and f(x) = a(e^(x/a) - 1) if x <= 0. The value of a is usually 1. The function is similar to the ELU function, but it has a different output when x < 0.

### 14. Softplus

The Softplus function is a smooth version of the ReLU function. The function is defined as f(x) = log(1 + e^x). The function is used in the GPT model.

## Conclusion

Activation functions are an essential part of neural networks. They help normalize the output of each neuron to a range between 1 and 0 or between -1 and 1. There are many different types of activation functions, each with its own advantages and disadvantages. The choice of activation function depends on the specific problem you are trying to solve.

## References

1. https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6
2. https://towardsdatascience.com/activation-functions-and-its-types-which-is-better-a9a5310cc8f

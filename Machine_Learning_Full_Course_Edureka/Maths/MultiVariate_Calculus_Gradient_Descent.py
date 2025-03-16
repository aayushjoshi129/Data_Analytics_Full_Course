# Multivariate calculus plays a crucial role in various aspects of machine learning, particularly in optimization algorithms and gradient-based methods for training models. Here are some key concepts of multivariate calculus relevant to machine learning:

# 1. Gradient: In multivariate calculus, the gradient of a function is a vector that points in the direction of the steepest increase of the function at a given point. In machine learning, gradients are used to optimize objective functions during training by iteratively adjusting model parameters to minimize (or maximize) the objective.

# 2. Partial Derivatives: Partial derivatives measure how a function changes with respect to each of its input variables while keeping the other variables constant. In machine learning, partial derivatives are used to compute gradients efficiently for models with multiple parameters.

# 3. Chain Rule: The chain rule states how to compute the derivative of a composite function. In machine learning, the chain rule is applied when calculating gradients through layers of neural networks or other complex models.

# 4. Jacobian Matrix: The Jacobian matrix generalizes the concept of the gradient to vector-valued functions. It represents the collection of all partial derivatives of a vector-valued function with respect to its input variables. In machine learning, the Jacobian matrix is used in optimization algorithms for functions with vector-valued outputs.

# 5. Hessian Matrix: The Hessian matrix contains the second partial derivatives of a scalar-valued function of multiple variables. It provides information about the curvature of the function's surface and is used in optimization algorithms to determine convergence properties and step sizes.

# 6. Optimization Algorithms: Multivariate calculus underpins various optimization algorithms used in machine learning, such as gradient descent, stochastic gradient descent, Adam, RMSprop, and others. These algorithms leverage derivatives and gradients to iteratively update model parameters and minimize a given objective function.

# Understanding multivariate calculus is essential for effectively designing, implementing, and optimizing machine learning models, especially deep learning models with numerous parameters. It provides the mathematical foundation for optimization algorithms that drive model training and learning.


# In machine learning, understanding the rules of differentiation is crucial for computing gradients efficiently, which is essential for training models using optimization algorithms like gradient descent. Let's go over some key rules of differentiation and how they are applied in machine learning, along with examples:

# 1. Sum Rule:
#    - Rule: The derivative of the sum of two functions is the sum of their derivatives.
#      \[ \frac{d}{dx} (f(x) + g(x)) = \frac{d}{dx} f(x) + \frac{d}{dx} g(x) \]
#    - Example: Suppose we have a loss function \( L(w) = L_1(w) + L_2(w) \), where \( L_1(w) \) and \( L_2(w) \) are two differentiable functions. The gradient of the loss function with respect to the parameters \( w \) is computed as the sum of the gradients of \( L_1(w) \) and \( L_2(w) \):
#      \[ \nabla_w L(w) = \nabla_w L_1(w) + \nabla_w L_2(w) \]

# 2. Product Rule:
#    - Rule: The derivative of the product of two functions is the first function times the derivative of the second function plus the second function times the derivative of the first function.
#      \[ \frac{d}{dx} (f(x) \cdot g(x)) = f(x) \cdot \frac{d}{dx} g(x) + g(x) \cdot \frac{d}{dx} f(x) \]
#    - Example: In neural networks, when computing the gradient of the loss function with respect to the parameters of a layer, the product rule is applied to the activation function and the weighted input to the layer.

# 3. Chain Rule:
#    - Rule: The chain rule allows us to compute the derivative of a composite function. If \( y = f(g(x)) \), then the derivative of \( y \) with respect to \( x \) is the derivative of \( f \) with respect to \( g \) multiplied by the derivative of \( g \) with respect to \( x \).
#      \[ \frac{dy}{dx} = \frac{dy}{dg} \cdot \frac{dg}{dx} \]
#    - Example: In backpropagation, which is used to compute gradients in neural networks, the chain rule is applied recursively to compute gradients layer by layer, starting from the output layer and moving backward through the network.

# These are some of the fundamental rules of differentiation applied in machine learning. They are used extensively in gradient-based optimization algorithms to update model parameters during training. Understanding these rules and how to apply them efficiently is essential for effectively training machine learning models.

# The formula you're referring to is called the power rule in calculus, which states that the derivative of a function of the form \( f(x) = x^n \) is \( f'(x) = nx^{n-1} \).

# Here's how it applies in the context of machine learning:

# Suppose we have a function \( f(x) = x^n \), where \( x \) represents a variable, and \( n \) is a constant exponent. In machine learning, this could represent various scenarios, such as:

# 1. Feature Transformation:
#    - Suppose \( x \) represents a feature in a dataset, and we want to transform it by raising it to a certain power \( n \). The derivative \( f'(x) = nx^{n-1} \) gives us the rate of change of the transformed feature with respect to the original feature.

# 2. Activation Functions:
#    - In neural networks, activation functions like the sigmoid function \( \sigma(x) = \frac{1}{1 + e^{-x}} \) and the ReLU function \( \text{ReLU}(x) = \max(0, x) \) involve raising the input \( x \) to a power. The power rule is applied when computing the derivative of these activation functions, which is essential for backpropagation during training.

# 3. Loss Functions:
#    - Some loss functions used in machine learning may involve terms like \( x^n \), where \( x \) represents predicted values and \( n \) is a constant exponent. The derivative of such loss functions with respect to the predicted values \( x \) would follow the power rule.

# In summary, the power rule \( f'(x) = nx^{n-1} \) is a fundamental concept in calculus that applies in various contexts within machine learning, including feature transformation, activation functions, and loss functions. Understanding this rule is essential for efficiently computing derivatives and training machine learning models.

# Gradient Descent

import numpy as np

def sigmoid(sop):
    return 1.0 / (1 + np.exp(-1 * sop)) # -> (1/(1+e^-sop))

def error(predicted, target):
    return np.power(predicted - target, 2) # (pred - tar)^2 or x^2

def error_predicted_deriv(predicted, target):
    return 2 * (predicted - target) # 2*(pred-tar) or 2x

def activation_sop_deriv(sop):
    return sigmoid(sop) * (1.0 - sigmoid(sop)) # actual function

def sop_w_deriv(x):
    return x

def update_w(w, grad, learning_rate):
    return w - learning_rate * grad # update the weight

x = 0.1
target = 0.3
learning_rate = 0.01
w = np.random.rand()
print("Initial Weight:", w)

for k in range(1000000):
    # Forward pass
    y = w*x
    predicted = sigmoid(y)
    err = error(predicted, target)

    # Backward Pass
    g1 = error_predicted_deriv(predicted, target)
    g2 = activation_sop_deriv(predicted)
    g3 = sop_w_deriv(x)

    grad = g3*g2*g1
    print(predicted)

    w = update_w(w, grad, learning_rate)


# COD WALK THROUGH

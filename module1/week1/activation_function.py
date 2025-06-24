import math


def sigmoid(x):
    """
    Compute the sigmoid activation function.

    Args:
        x (float): Input value.

    Returns:
        float: The sigmoid of x = 1 / (1 + exp(-x)).
    """
    return 1. / (1 + math.exp(-x))

def relu(x):
    """
    Compute the Rectified Linear Unit (ReLU) activation function.

    Args:
        x (float): Input value.

    Returns:
        float: The ReLU activation of x, defined as:
               - 0 if x <= 0
               - x if x > 0
    """
    return 0 if x <= 0 else x

def elu(x : float) -> float:
    """
    Compute the Exponential Linear Unit (ELU) activation function.

    Args:
        x (float): Input value.
        alpha = CONSTANT = 0.1 in this function

    Returns:
        float: The ELU activation of x, calculated as:
               - x if x > 0
               - alpha * (exp(x) - 1) if x <= 0
    """
    return x if x > 0 else 0.1 * (math.exp(x) -1)

def is_number(n):
    try: 
        float(n)
    
    except ValueError:
        return False
    return True

def main():
    x = input("Enter a number for activation function:")

    if is_number(x):
        x = float(x)
        activation_type = input("Choose an activation fuction type (sigmoid | relu | elu:) ")
        if activation_type.lower() == "sigmoid":
            activation_value = sigmoid(x)
        elif activation_type.lower() == "relu":
            activation_value = relu(x)
        elif activation_type.lower() == "elu":
            activation_value = elu(x)
        else: 
            print(f'Do not support {activation_type} activation function. Please choose one of three this function, sigmoid | relu | elu!')
            return None
        activation_type = activation_type.capitalize()
        print(f"{activation_type}: f({x}) = {activation_value}")
        return activation_value
    else: 
        print(f'Please enter an number!')
main()


    
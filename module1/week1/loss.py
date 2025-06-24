import random
import math 



def is_integer(x):
    if not isinstance(x, int):
        print(f'{x} must be int')
        return False
    else:
        return True
    




def main():
    try:
        x = int(input('Please enter an integer as the number of sample: '))
    except ValueError:
        print('The number of sample must be an integer')
    
    loss_name = input("Please enter type of loss name (MAE | MSE): ")

    target = []
    predict = []
    loss = 0
    loss_sum=0
    for i in range(x):
        target.append(random.uniform(0,10))
        predict.append(random.uniform(0,10))
        if loss_name.lower() == "mae":
            loss = abs(target[i]- predict[i])
        elif loss_name.lower() == "mse":
            loss = math.pow((target[i]- predict[i]),2)
        loss_sum += loss
        print(f'Loss_name: {loss_name.capitalize()}, sample {i}:  pred: {predict[i]}, target: {target[i]}, loss: {loss}')
    avg_loss = loss_sum / x
    print(f'final {loss_name}: {avg_loss}')

    
main()

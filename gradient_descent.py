import random

step_size = 0.01
precision = 0.00001

def main():
    x = random.randrange(1,100)
    new_x = 0
    i = 0
    while abs((x - step_size * f_prime(x))) > precision :
        new_x = x - step_size * f_prime(x)
        print(f'{i+1}: {round(x,6)} -> {round(new_x,6)}\n')
        x = new_x
        i += 1
    print(f'total: {i+1} | RESULT = {x}\n')

def f_prime(x):
    return 2*x

if __name__ == '__main__':
    main()

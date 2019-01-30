def fibonacci(n):
    index = 0
    result = 1
    sum = 0
    for i in range(n):
        sum = sum + index + result
        index =+ 1
        result =+ 1
    print('The sum =', sum)
    return sum

n_input = int(input('Please, write a number n: '))
fibonacci(n_input)
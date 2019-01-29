def fibonacci(n):
    global counter
    index = 0
    result = 1
    counter = 0
    sum = 0
    for i in range(n):
        sum = sum + index + result
        index =+ 1
        result =+ 1
        counter =+ 1
    return sum

n_input = int(input('Please, write a number n: '))
fibonacci(n_input)
print('The number ', n_input, ' is the ', counter, 'th number of fibonacci\'s sequence')

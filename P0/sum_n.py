sum_input = int(input('Please, insert a number: '))

def sum_n(n):
    result = 0
    for number in range(n):
        result = result + (number) + 1
    print(result)

    return result
sum_n(sum_input)



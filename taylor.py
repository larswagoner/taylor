

A = 0


def factorial(n):
    result = 1
    for number in range(1, n+1):
        result *= number
    return result


#splits up the function in accordance to the manual's instructions
def separate_function(function):
    function = function.split('+')
    terms = []
    for term in function:
        term = term.split('^')
        term = [list(map(int, term))]
        terms += term
    return terms


#obtains coefficients and exponents of the polynomial for ease of use
def deconstruct_polynomial(polynomial):
    coefficients = [term[0] for term in polynomial]
    exponents = [term[1] for term in polynomial]

    return coefficients, exponents


def evaluate_polynomial(coefficients, exponents, variable):
    result = 0
    for coefficient, exponent in zip(coefficients, exponents):
        result += coefficient * (variable ** exponent)

    return result


def differentiate_polynomial(coefficients, exponents):
    new_coefficients = []

    for coefficient, exponent in zip(coefficients, exponents):
        new_coefficients += [coefficient * exponent]

    exponents = [number - 1 if number != 0 else 0 for number in exponents]

    return new_coefficients, exponents


def taylor(f, x, n):
    coefficients, exponents = deconstruct_polynomial(f)
    approximation = 0

    for number in range(0, n):
        approximation += (evaluate_polynomial(coefficients, exponents, A) * ((x - A)**number)) / factorial(number)
        coefficients, exponents = differentiate_polynomial(coefficients, exponents)

    return approximation


def start(file_name, n):
    lines = open(file_name).read().splitlines()

    for line in lines:
        line = line.split('=')
        x = int(line[0])
        function = separate_function(line[1])

        print('The approximation achieved using a Maclaurin series of %d terms is %.1f.' % (n, taylor(function, x, n)))


#start
file_name = input('Enter the file name to approximate with a Maclaurin series: ')
n = int(input('How many terms in the Maclaurin series would you like: '))

start(file_name, n)

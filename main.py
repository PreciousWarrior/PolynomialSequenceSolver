# TODO error handling and more testing

import numpy

# Get the value of n where the nth difference of the series is constant;
# or get the degree of the polynomial that can be used to model the series
def get_polynomial_degree(sequence, n=0):
    if len(sequence) <= 1:
        return None
    if sequence.count(sequence[0]) == len(sequence):
        return n
    differences = []
    for index in range(1, len(sequence)):
        difference = sequence[index] - sequence[index-1] 
        differences.append(difference)
    return get_polynomial_degree(differences, n+1)


def get_general_rule(sequence, degree):
    sequence = sequence[0:degree+1]
    sol_matrix = []
    poly_matrix = []
    for index, term in enumerate(sequence):
        sol_matrix.append([term])
        polynomial_array = []
        for power in range(degree, -1, -1):
            polynomial_array.append((index+1)**power)
        poly_matrix.append(polynomial_array)
    inverted = numpy.linalg.inv(numpy.array(poly_matrix))
    final = numpy.ndarray.tolist(numpy.dot(inverted, numpy.array(sol_matrix)))
    return [x[0] for x in final]



superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹" }

trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))

if __name__ == "__main__":
    sequence = input("Enter a sequence seperated by spaces: ").split(" ")
    sequence = [float(x) for x in sequence]
    degree = get_polynomial_degree(sequence)
    rule = get_general_rule(sequence, degree)
    output = "f(n)="
    for index, term in enumerate(rule):
        power = len(rule) - index -  1
        power_str = str(power).translate(trans)
        term = round(term, 4)
        sign = "+"
        if index == 0:
            sign = ""
        if term == 0:
            continue
        if term < 0:
            sign = "-"
        if term.is_integer():
            term = int(term)
        if power > 2:
            output += f"{sign}{abs(term)}n{power_str}"
        if power == 1:
            output += f"{sign}{abs(term)}n"
        if power == 0:
            output += f"{sign}{abs(term)}"
    print(output)


'''

    sequence_null = [1]
    sequence_0 = [9, 9, 9, 9, 9, 9]
    sequence_1 = [2, 4, 6, 8, 10]
    sequence_2 = [2, 5, 9, 14, 20]
    sequence_3 = [4, 32, 108, 256, 500]
'''

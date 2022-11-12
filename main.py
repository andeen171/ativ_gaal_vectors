import math
import numpy as np

def format_system(vec: list[str], dot: list[str]) -> str:
    return f'    x = {dot[0]} + {vec[0]}t\n' \
           f'r:  y = {dot[1]} + {vec[1]}t\n' \
           f'    z = {dot[2]} + {vec[2]}t\n'


def question_1():
    vec = input('Digite o vetor, ex.: a b c:\n').split(' ')
    dot = input('Digite o ponto, ex.: x y z:\n').split(' ')
    print(format_system(vec, dot))


def format_eq(vec: list[str], d: float) -> str:
    return f'π: {vec[0]}x + {vec[1]}y + {vec[2]}z + {d} = 0'


def question_2():
    norma = input('Digite a norma do vetor, ex.: a b c\n').split(' ')
    a = float(norma[0])
    b = float(norma[1])
    c = float(norma[2])

    dot = input('Digite o ponto, ex.: x y z:\n').split(' ')
    x = float(dot[0])
    y = float(dot[1])
    z = float(dot[2])

    d = -((a * x) + (b * y) + (c * z))
    print(format_eq(norma, d))


def question_3():
    plane_eq = input('Digite a equação do plano sem as variaveis, ex.: "a b c d":\n').split(' ')
    a = float(plane_eq[0])
    b = float(plane_eq[1])
    c = float(plane_eq[2])
    d = float(plane_eq[3])

    dot = input('Digite o ponto, ex.: "x y z":\n').split(' ')
    x = float(dot[0])
    y = float(dot[1])
    z = float(dot[2])

    result = abs((a * x) + (b * y) + (c * z) + d) / \
        math.sqrt((a ** 2) + (b ** 2) + (c ** 2))
    print(f'd(P,α) = {result}')


def norma(vec: list[float]):
    return math.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)


def question_4():
    print('Digite o sistema que define a reta!')
    x_eq = input('x = ').split(' ')
    x = float(x_eq[0])
    a = float(x_eq[1])

    y_eq = input('y = ').split(' ')
    y = float(y_eq[0])
    b = float(y_eq[1])

    z_eq = input('z = ').split(' ')
    z = float(z_eq[0])
    c = float(z_eq[1])

    dot = input('Digite o ponto, ex.: "x y z":\n').split(' ')
    dot_vec = [float(dot[0]) - x, float(dot[1]) - y, float(dot[2]) - z]
    result = norma([a - dot_vec[0], b - dot_vec[1], c - dot_vec[2]]) / norma([a, b, c])

    print(f'd(P,α) = {result}')


def question_5():
    plane_1_eq = input(
        'Digite a equação do primeiro plano sem as variaveis, ex.: "a b c d":\n').split(' ')
    plane_1_eq = [float(i) for i in plane_1_eq]

    plane_2_eq = input(
        'Digite a equação do plano sem as variaveis, ex.: "a b c d":\n').split(' ')
    plane_2_eq = [float(i) for i in plane_2_eq]
    
    if (plane_1_eq[0] / plane_2_eq[0]) == (plane_1_eq[1] / plane_2_eq[1]) == (plane_1_eq[2] / plane_2_eq[2]):
        dot_x = -plane_1_eq[3] / plane_1_eq[0]
        result = abs((plane_2_eq[0] * dot_x) + plane_2_eq[3]) / \
            math.sqrt((plane_2_eq[0] ** 2) + (plane_2_eq[1] ** 2) + (plane_2_eq[2] ** 2))
        print(result)
    else:
        print("Os dois planos são concorrentes logo a distância é zero")


def question_6():
    print('Digite o sistema que define a primeira reta!')
    x = input('x = ').split(' ')
    x_1 = [float(i) for i in x]
    y = input('y = ').split(' ')
    y_1 = [float(i) for i in y]
    z = input('z = ').split(' ')
    z_1 = [float(i) for i in z]

    print('Digite o sistema que define a segunda reta!')
    x = input('x = ').split(' ')
    x_2 = [float(i) for i in x]
    y = input('y = ').split(' ')
    y_2 = [float(i) for i in y]
    z = input('z = ').split(' ')
    z_2 = [float(i) for i in z]
    if (x_1[1] / x_2[1]) == (y_1[1] / y_2[1]) == (z_1[1] / z_2[1]):
        dot = [x_1[0], y_1[0], z_1[0]]
        dot_vec = [dot[0] - x_2[0], dot[1] - y_2[0], dot[2] - z_2[0]]
        result = norma([x_2[1] - dot_vec[0], y_2[1] - dot_vec[1],z_2[1] - dot_vec[2]]) / \
            norma([x_2[1], y_2[1], z_2[1]])
        print(result)
    else:
        matrix = [
            [x_1[1], y_1[1], z_1[1]],
            [x_2[1], y_2[1], z_2[1]],
            [x_2[0] - x_1[0], y_2[0] - y_1[0], z_2[0] - z_1[0]]
        ]
        np_matrix = np.array(matrix)
        det = abs(np.linalg.det(np_matrix))
        product = np.cross(matrix[0], matrix[1])
        norma_ = math.sqrt(product[0] ** 2 + product[1] ** 2 + product[2] ** 2)
        result = det / norma_
        print(result)


if __name__ == '__main__':
    option = input('Digite o número da questão:\n')
    match option:
        case '1':
            question_1()
        case '2':
            question_2()
        case '3':
            question_3()
        case '4':
            question_4()
        case '5':
            question_5()
        case '6':
            question_6()

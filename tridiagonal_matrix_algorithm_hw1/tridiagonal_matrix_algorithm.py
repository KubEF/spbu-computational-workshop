import helpers
from prettytable import PrettyTable


def tridiagonal_algorithm_with_coefficients(
        a_values: list[float],
        b_values: list[float],
        c_values: list[float],
        d_values: list[float]) -> (list[float], list[float], list[float]):
    l = len(a_values)
    if not (len(a_values) == len(b_values) and len(b_values) == len(c_values) and len(c_values) == len(d_values)):
        raise ValueError("lens of lists cannot be different")
    m = [0.0] * l
    k = [0.0] * l
    y = [0.0] * l
    m[0] = (-c_values[0]) / (b_values[0])
    k[0] = (d_values[0]) / (b_values[0])
    for i in range(1, l):
        m[i] = -(c_values[i - 1]) / (a_values[i - 1] * m[i - 1] + b_values[i - 1])
        k[i] = (d_values[i - 1] - a_values[i - 1] * k[i - 1]) / (a_values[i - 1] * m[i - 1] + b_values[i - 1])

    y[l - 1] = (d_values[l - 1] - a_values[l - 1] * k[l - 1]) / (b_values[l - 1] + a_values[l - 1] * m[l - 1])
    for i in range(l - 2, -1, -1):
        y[i] = m[i + 1] * y[i + 1] + k[i + 1]
    return m, k, y


# y'' + 6y = -x, то есть p(x) === 1, q(x) === 0, r(x) === 6, f(x) = -x
# y(0) = 0, y(1) = 0, то есть alpha_0 = 1, alpha_1 = 0, beta_0 = 1, beta_1 = 0, A = 0, B = 0
# границы [0; 1], то есть a = 0, b = 1
def f(x):
    return -x


def p(x):
    return 1


def q(x):
    return 0


def r(x):
    return 6.0


if __name__ == "__main__":
    n = int(input("Введите количество точек: "))
    xs = helpers.generate_xs(0, 1, n)
    h = 1 / n

    A_values = [0.0]
    B_values = [h]
    C_values = [0.0]
    D_values = [0.0]
    for x in xs[1:n]:
        A_values.append(p(x) - h * q(x) / 2)
        B_values.append(-2 * p(x) + h * h * r(x))
        C_values.append(p(x) + h * q(x) / 2)
        D_values.append(h * h * f(x))
    A_values.append(0.0)
    B_values.append(h)
    C_values.append(0.0)
    D_values.append(0.0)

    m, k, y = tridiagonal_algorithm_with_coefficients(A_values, B_values, C_values, D_values)

    table = PrettyTable()
    table.add_column("x_i", xs)
    table.add_column("A_i", A_values)
    table.add_column("B_i", B_values)
    table.add_column("C_i", C_values)
    table.add_column("D_i", D_values)
    table.add_column("m_i", m)
    table.add_column("k_i", k)
    table.add_column("y_i", y)
    print(table)

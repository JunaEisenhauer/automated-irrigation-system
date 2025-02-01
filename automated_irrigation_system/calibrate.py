MIN_VALUE = 0.34294088910600884
MAX_VALUE = 0.723009281875916
SPACE = 0.02


def calculate_gradient_and_offset(min_value, max_value, space):
    gradient = 100 / (max_value - min_value + 2 * space)
    offset = -(min_value - space) * gradient
    return gradient, offset


if __name__ == '__main__':
    m, b = calculate_gradient_and_offset(MIN_VALUE, MAX_VALUE, SPACE)
    print("Gradient: " + str(m) + ", Offset: " + str(b))

from math import sqrt


def prepare_pattern(pattern):
    value_pattern = list(pattern.replace('#', '1').replace('-', '0'))
    value = list(map(int, value_pattern))
    x = sum(value)
    root = sqrt(x)
    for index, number in enumerate(value):
        value[index] /= root
    return value


def read_data(file):
    with open(file, newline='') as file:
        data = file.read().strip().split('\r\n')

    letters = []
    patterns = []
    number_of_patterns = int(data.pop(0))
    horizontal = int(data.pop(0))
    vertical = int(data.pop(0))

    for i in range(number_of_patterns):
        letter = data.pop(0)
        pattern = ''
        for row in range(horizontal):
            pattern += data.pop(0)
        patterns.append(prepare_pattern(pattern))
        letters.append(letter)
    return letters, patterns


def training_data(data):
    patterns = data[1]
    weights = []
    layers = []

    for i in range(len(patterns)):
        for j in range(len(patterns[i])):
            weight = patterns[i][j]
            weights.append(weight)
        layers.append(weights)
        weights = []
    return layers


def compute(test, layer, layer_index):
    value = 0
    for i in range(len(layer[layer_index])):
        value += layer[layer_index][i] * test[i]
    return value


def madaline(layer, test_data):
    outputs = []
    layer_index = 0
    for letter in test_data[0]:
        print(f'Letter {letter}')
        for test in test_data[1]:
            output = compute(test, layer, layer_index)
            print(output)
            outputs.append(output)
        found_result = max(outputs)
        found_letter = test_data[0][outputs.index(found_result)]
        layer_index += 1
        outputs = []
        print(f'Letter {found_letter} was recognized. Level of confidence = {round(found_result, 2)}')


train_data = read_data('train.txt')
test_data = read_data('test.txt')
layer = training_data(train_data)
madaline(layer, test_data)

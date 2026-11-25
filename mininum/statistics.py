import math


def sum(self):
    sum = 0

    for x in self.data:
        sum += x

    return sum


def min(self):
    if len(self.data) == 0:
        raise ValueError("Cannot find minimum of an empty array")

    minimum = self.data[0]

    for x in self.data:
        minimum = x if x < minimum else minimum

    return minimum


def max(self):
    if len(self.data) == 0:
        raise ValueError("Cannot find maximum of an empty array")

    maximum = self.data[0]

    for x in self.data:
        maximum = x if x > maximum else maximum

    return maximum


def mean(self):
    sum = 0

    for x in self.data:
        sum += x

    return sum / len(self.data)


def median(self):
    if len(self.data) == 0:
        raise ValueError("Cannot calculate median of an empty array")

    sorted_data = sorted(self.data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]

        return (middle1 + middle2) / 2


def variance(self):
    if len(self.data) == 0:
        raise ValueError("Cannot calculate variance of an empty array")

    avg = mean(self)
    sum = 0

    for x in self.data:
        sum += (x - avg) ** 2

    return sum / len(self.data)


def standard_deviation(self):
    return math.sqrt(variance(self))


def argmin(self):
    if len(self.data) == 0:
        raise ValueError("Cannot find argmin of an empty array")

    argmin = 0

    for i in range(1, len(self.data)):
        argmin = i if self.data[i] < self.data[argmin] else argmin

    return argmin


def argmax(self):
    if len(self.data) == 0:
        raise ValueError("Cannot find argmax of an empty array")

    argmax = 0

    for i in range(1, len(self.data)):
        argmax = i if self.data[i] > self.data[argmax] else argmax

    return argmax


def count(self, value):
    # o for no occurrences
    counter = 0

    for x in self.data:
        if x == value:
            counter += 1

    return counter


def unique(self):
    result = []

    for x in self.data:
        if x not in result:
            result.append(x)

    return result

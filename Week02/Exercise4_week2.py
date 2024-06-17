# Levenshtein distance
import math
import numpy
import string

source = ' '
target = ' '
m = 0
n = 0

del_cost = 0
ins_cost = 0
sub_cost = 0

matrix_list = []


def levenshtein_distance(source, target):
    # Create a matrix with m lines and n columns with all 0. m = len(source) + 1, n = len(target) + 1
    m = len(source) + 1
    n = len(target) + 1
    l_distance = numpy.zeros((m, n))

    for i in range(0, m):
        l_distance[i][0] = i    # create the first column

    for j in range(0, n):
        l_distance[0][j] = j    # create the first line


    for i in range(1, m):
        for j in range(1, n):
            if (source[i-1] == target[j-1]):
                l_distance[i][j] = l_distance[i-1][j-1]
            else:
                del_cost = l_distance[i-1][j]
                ins_cost = l_distance[i][j-1]
                sub_cost = l_distance[i-1][j-1]
                matrix_list = [del_cost, ins_cost, sub_cost]
                l_distance[i][j] = 1 + min(matrix_list)


    return l_distance[len(source)][len(target)]


if __name__ == "__main__":
    source_ex = "hola"
    target_ex = "hello"
    print(levenshtein_distance(source_ex, target_ex))

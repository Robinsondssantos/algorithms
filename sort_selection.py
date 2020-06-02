# Encontre o menor valor;
# Troque o menor valor com o primeiro item do array;
# Encontre o segundo menor valor;
# Troque o segundo menor valor com o segundo item do array;
# Repita a operação até o array estar ordenado.

# Example:
# x[0] > x[1]
# x[0] > x[2]
# x[0] > x[3]

# x[1] > x[2]
# x[1] > x[3]

# x[2] > x[4]

# Source: https://klauslaube.com.br/2019/05/10/algoritmos-de-ordenacao-parte-1.html


def sort_selection(array):

    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    i = len(array) - 1
    k = 0

    while i > 0:
        for j in range(i):
            if array[k] > array[j+k+1]:
                swap(k, j+k+1)

        k += 1
        i -= 1

    return array


def reverse_sort_selection(array):

    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    i = len(array) - 1

    while i > 0:
        for j in range(i):
            if array[i] < array[j]:
                swap(i, j)
        i -= 1
    
    return array


if __name__ == '__main__':
    print('sort_selection:', 
      sort_selection([12, 15, 42, 53, 26, 59, 86, 75, 48, 74, 45, 65, 21, 23, 98, 87]))
    print('reverse_sort_selection:', 
      reverse_sort_selection([12, 15, 42, 53, 26, 59, 86, 75, 48, 74, 45, 65, 21, 23, 98, 87]))      
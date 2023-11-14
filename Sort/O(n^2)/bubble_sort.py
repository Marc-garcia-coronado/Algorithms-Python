def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            #  len(array) - i - 1: La razón detrás de len(array) - i - 1 es que,
            #  después de cada iteración externa del bucle (el bucle principal
            #  que itera sobre todos los elementos de la lista), el elemento más
            #  grande ya está en su posición correcta en la parte derecha de la lista.
            #  Por lo tanto, no es necesario considerar esos elementos ya ordenados
            #  en las iteraciones posteriores. Restando i del tamaño total de la lista,
            #  nos aseguramos de no comparar y ordenar los elementos que ya están en su posición correcta.
            
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

    return array


def main():
    """
    bubble sort = pairs of adjacent elements are compared, and the elements
                  swapped if they are not in order.

                  Quadratic time O(n^2)
                  small data set = okay-ish
                  large data set = bad
    """

    array = [9, 2, 5, 4, 7, 1, 3, 6, 8]

    array = bubble_sort(array)

    for i in array:
        print(i)


if __name__ == '__main__':
    main()

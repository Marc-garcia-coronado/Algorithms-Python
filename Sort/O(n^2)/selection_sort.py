def selection_sort(array):

    for i in range(len(array)):
        minim = i
        for j in range(i + 1, len(array)):
            if array[minim] > array[j]:
                minim = j
        temp = array[i]
        array[i] = array[minim]
        array[minim] = temp

    return array


def main():
    """
    selection sort = search through an array and keep track of the minimum
                     value during each iteration. At the end of each iteration,
                     we swap variables.

                     Quadratic time O(n^2)
                     small data set = okay
                     large data set = BAD

    """

    array = [5, 3, 6, 1, 2, 9, 4, 7, 8]

    array = selection_sort(array)

    for i in array:
        print(i)


if __name__ == '__main__':
    main()

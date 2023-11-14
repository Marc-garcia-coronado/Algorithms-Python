def insertion_sort(array):

    for i in range(len(array)):
        temp = array[i]
        j = i - 1

        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp

    return array


def main():
    """
    insertion sort = after comparing elements to the left
                    shift elements to the right to make room to insert a value

                    Quadratic time O(n^2)
                    small data set = decent
                    large data set = BAD
                    Less steps than Bubble Sort
                    Best case is O(n) compared to Selection Sort O(n^2)
    """

    array = [9, 1, 8, 2, 7, 3, 6, 5, 4]

    array = insertion_sort(array)

    for i in array:
        print(i)


if __name__ == '__main__':
    main()

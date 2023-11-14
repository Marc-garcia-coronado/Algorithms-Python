def merge(left_array, right_array, array):

    # Indices i = iteration, l = left index, r = right index
    i = l = r = 0

    # Check the conditions for merging
    # Merge the two halves back together
    while l < len(left_array) and r < len(right_array):
        if left_array[l] < right_array[r]:
            array[i] = left_array[l]
            i += 1
            l += 1
        else:
            array[i] = right_array[r]
            i += 1
            r += 1
    # Check if there are any remaining elements in the left half
    while l < len(left_array):
        array[i] = left_array[l]
        i += 1
        l += 1
    # Check if there are any remaining elements in the right half
    while r < len(right_array):
        array[i] = right_array[r]
        i += 1
        r += 1


def merge_sort(array):

    length = len(array)

    if length <= 1:
        return 1

    middle = length // 2

    left_array = array[:middle]
    right_array = array[middle:]

    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, array)

    return array


def main():

    array = [8, 2, 5, 3, 4, 7, 6, 1]
    print(f"Unsorted array {array}")

    merge_sort(array)
    print(f"\nSorted array {array}")


if __name__ == '__main__':
    main()

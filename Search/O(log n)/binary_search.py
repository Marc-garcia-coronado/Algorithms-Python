def binary_search(array, target):

    low = 0
    high = len(array) - 1
    steps = 0

    while low <= high:
        steps += 1
        middle = (low + high) // 2
        # Middle is equal to the low which initially is 0 + high which is len(array) // 2
        # // 2 rounds it up so its like doing round()
        value = array[middle]
        print(f"middle: {middle}")

        if value < target:
            # If the target is greater than middle, search in the right half of the array
            low = middle + 1
        elif value > target:
            # If the target is less than middle, search in the left half of the array
            high = middle - 1
        else:
            return middle, steps  # Target found

    return -1  # Target not found


def main():
    """
    Binary search = Search algorithm that finds the position of a target
                    value within a sorted array.
                    Half of the array is eliminated during each "step".
    """
    array = []
    target = 340

    for i in range(10000):
        array.append(i)

    index = binary_search(array, target)

    if index != 1:
        print(f"Target found at index {index}")
    else:
        print(f"Target not found")


if __name__ == '__main__':
    main()

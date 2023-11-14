def interpolation_search(array, target):

    high = len(array) - 1
    low = 0

    while target >= array[low] and target <= array[high] and low <= high:
        probe = low + (high - low) * (target - array[low]) // (array[high] - array[low])
        print(f"probe: {probe}")

        if array[probe] == target:
            return probe
        elif array[probe] < target:
            low = probe + 1
        else:
            high = probe - 1

    return -1


def main():
    """
    interpolation search = improvement over binary search best used for "uniformly" distributed "guesses"
                           where a value might be based on calculated probe results if probe is incorrect,
                           search area is narrowed, and a new probe is calculated

                           average case: O(log(log(n)))
                           worst case: O(n) [values increase exponentially]
    """
    array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    index = interpolation_search(array, 256)

    if index != -1:
        print(f"Target found at index {index}")
    else:
        print(f"Target not found")


if __name__ == '__main__':
    main()

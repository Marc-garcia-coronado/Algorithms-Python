def walk(steps):

    if steps < 1:
        return
    print("You take a step ")
    walk(steps - 1)

    return 0


def factorial(num):

    """
    7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5040
    """
    if num < 1:
        return 1  # base case
    else:
        return num * factorial(num - 1)  # recursive


def power(base: int, exponent: int):

    if exponent < 1:
        return 1  # base case
    else:
        # print("step")
        power_case = power(base, exponent - 1)
        return base * power_case   # recursive case


def main():
    """
    recursion = When a thing is defined in terms of itself.
                Apply the result of a procedure, to a procedure.
                A recursive method calls itself. Can be a substitute for iteration.
                Divide a problem into sub-problems of the same type as the original.
                Commonly used with advanced sorting algorithms and navigating trees

                Advantages
                ----------
                easier to read/write
                easier to debug

                Disadvantages
                -------------
                sometimes slower
                uses more memory
    """

    # walk(5)
    # print(factorial(7))
    print(power(2, 8))


if __name__ == '__main__':
    main()

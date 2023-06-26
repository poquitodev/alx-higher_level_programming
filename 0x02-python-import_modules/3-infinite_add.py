#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total_sum = 0
    for j in range(len(sys.argv) - 1):
        total_sum += int(sys.argv[j + 1])
    print("{}".format(total_sum))

#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv)
    ds = length - 1

    if ds == 0:
        print("0 arguments.")
    else:
        if ds == 1:
            print(f"{ds} argument:")
        else:
            print(f"{ds} arguments:")

        for i in range(1, length):
            print(f"{i}: {argv[i]}")

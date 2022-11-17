#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that prints out every RGB value


def main():
    # Prints out every RGB value

    dummy_value = input("\nPress Enter to start printing all RGB values.\n")
    for r_value in range(0, 256):
        for g_value in range(0, 256):
            for b_value in range(0, 256):
                print("R {0} G {1} B {2}".format(r_value, g_value, b_value))
    print("\nDone.")


if __name__ == "__main__":
    main()
